'''
Created on 19 juin 2020

@author: tleduc
'''
import unittest

from geopandas.geodataframe import GeoDataFrame
from shapely.geometry import LineString
from t4gpd.demos.GeoDataFrameDemos import GeoDataFrameDemos
from t4gpd.morph.geoProcesses.Diameter import Diameter
from t4gpd.morph.geoProcesses.STGeoProcess import STGeoProcess


class DiameterTest(unittest.TestCase):

    def setUp(self):
        self.buildings = GeoDataFrameDemos.ensaNantesBuildings()

    def tearDown(self):
        self.buildings = None

    def testRun(self):
        result = STGeoProcess(Diameter, self.buildings).run()

        self.assertIsInstance(result, GeoDataFrame, 'Is a GeoDataFrame')
        self.assertEqual(44, len(result), '44 rows')
        self.assertEqual(5, len(result.columns), '3 columns')

        for _, row in result.iterrows():
            self.assertIsInstance(row.geometry, LineString, 'Is a GeoDataFrame of LineString')
            self.assertIsInstance(row['diam_len'], float, 'Test diam_len attribute')
            self.assertTrue(0 < row['diam_len'] < 103.0, 'Test diam_len attribute')
            self.assertIsInstance(row['diam_azim'], float, 'Test diam_azim attribute')
            self.assertTrue(0 < row['diam_azim'] < 180.0, 'Test diam_len attribute')

        '''
        import matplotlib.pyplot as plt
        my_map_base = self.buildings.plot(color='lightgrey', edgecolor='black', linewidth=0.3)
        result.plot(ax=my_map_base, color='red', linewidth=0.7)
        plt.show()
        '''
        # result.to_file('/tmp/xxx.shp')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testRun']
    unittest.main()
