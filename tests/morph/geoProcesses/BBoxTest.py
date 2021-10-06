'''
Created on 16 juin 2020

@author: tleduc
'''
import unittest

from geopandas.geodataframe import GeoDataFrame
from shapely.geometry import Polygon
from t4gpd.demos.GeoDataFrameDemos import GeoDataFrameDemos
from t4gpd.morph.geoProcesses.BBox import BBox
from t4gpd.morph.geoProcesses.STGeoProcess import STGeoProcess


class BBoxTest(unittest.TestCase):

    def setUp(self):
        self.buildings = GeoDataFrameDemos.ensaNantesBuildings()

    def tearDown(self):
        self.buildings = None

    def testRun(self):
        result = STGeoProcess(BBox, self.buildings).run()

        self.assertIsInstance(result, GeoDataFrame, 'Is a GeoDataFrame')
        self.assertEqual(44, len(result), '44 rows')
        self.assertEqual(3, len(result.columns), '3 columns')

        shapeAreas = self.buildings.area
        inputShapes = self.buildings.geometry
        for i, row in result.iterrows():
            self.assertIsInstance(row.geometry, Polygon, 'Is a GeoDataFrame of Polygons')
            self.assertEqual(5, len(row.geometry.exterior.coords), 'Is a GeoDataFrame of quadrilaterals')
            self.assertLessEqual(shapeAreas[i], row.geometry.area, 'Areas test')
            self.assertTrue(inputShapes[i].within(row.geometry.buffer(0.001)), 'Within test')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
