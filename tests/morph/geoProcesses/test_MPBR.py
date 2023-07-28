'''
Created on 15 dec. 2020

@author: tleduc

Copyright 2020 Thomas Leduc

This file is part of t4gpd.

t4gpd is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

t4gpd is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with t4gpd.  If not, see <https://www.gnu.org/licenses/>.
'''
import unittest
from shapely.geometry import Polygon
from geopandas.geodataframe import GeoDataFrame
from t4gpd.morph.geoProcesses.STGeoProcess import STGeoProcess
from t4gpd.morph.geoProcesses.MPBR import MPBR


class MPBRTest(unittest.TestCase):

    def setUp(self):
        self.inputGeom = Polygon([(1, 0), (3, 0), (4, 1), (3, 1.9), (1, 1.9), (0, 1), (1, 0)])
        self.inputGdf = GeoDataFrame([{'geometry': self.inputGeom}])

    def tearDown(self):
        pass

    def testRun(self):
        result = STGeoProcess(MPBR, self.inputGdf).run()

        self.assertIsInstance(result, GeoDataFrame, 'Is a GeoDataFrame')
        self.assertEqual(1, len(result), 'Count rows')
        self.assertEqual(3, len(result.columns), 'Count columns')

        for _, row in result.iterrows():
            rect, len1, len2 = row[['geometry', 'mpbr_len1', 'mpbr_len2']]

            self.assertIsInstance(row.geometry, Polygon, 'Is a GeoDataFrame of Polygons')
            self.assertTrue(len1 >= len2, 'mpbr_len1 and mpbr_len2 attributes test (1)')
            self.assertAlmostEqual(len1 * len2, rect.area, 9, 'mpbr_len1 and mpbr_len2 attributes test (2)')
            self.assertAlmostEqual(len1, len2, 9, 'mpbr_len1 and mpbr_len2 attributes test (3)')
            self.assertAlmostEqual(11.314, rect.length, 2, 'Perimeter test')

        '''
        import matplotlib.pyplot as plt
        _, basemap = plt.subplots(figsize=(1 * 8.26, 1 * 8.26))
        result.boundary.plot(ax=basemap, color='grey')
        self.inputGdf.plot(ax=basemap, color='red')
        plt.show()
        '''


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
