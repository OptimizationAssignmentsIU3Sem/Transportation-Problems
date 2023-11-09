import unittest
import numpy as np
from algorithms import north_west, vogel, russell


class SimplexTestCase(unittest.TestCase):
    def testCaseNorthWest1(self):  # test method names begin with 'test'
        _costs = np.array([[2, 3, 4, 2, 4],
                           [8, 4, 1, 4, 1],
                           [9, 7, 3, 7, 2]])
        _demand = np.array([60, 70, 120, 130, 100])
        _supply = np.array([140, 180, 160])

        correct_X = [(0, 0, 60), (0, 1, 70), (0, 2, 10), (1, 2, 110), (1, 3, 70), (2, 3, 60), (2, 4, 100)]
        correct_Z = 1380

        x, z = north_west(_costs, _demand, _supply)
        self.assertTrue(set(correct_X) == set(x))
        self.assertEqual(correct_Z, z)

    def testCaseNorthWest2(self):
        costs = np.array([[7, 8, 1, 2],
                          [4, 5, 9, 8],
                          [9, 2, 3, 6]])
        demand = np.array([120, 50, 190, 110])
        supply = np.array([160, 140, 170])

        x, z = north_west(costs, demand, supply)
        correct_X = [(0, 0, 120), (0, 1, 40), (1, 1, 10), (1, 2, 130), (2, 2, 60), (2, 3, 110)]
        correct_Z = 3220
        self.assertTrue(set(correct_X) == set(x))
        self.assertEqual(correct_Z, z)

    def testCaseNorthWest3(self):
        # https://byjus.com/maths/north-west-corner-rule/
        _costs = np.array([[11, 13, 17, 14],
                           [16, 18, 14, 10],
                           [21, 24, 13, 10]])
        _demand = np.array([200, 225, 275, 250])
        _supply = np.array([250, 300, 400])

        sol, z = north_west(_costs, _demand, _supply)

        expected_X = [(0, 0, 200), (0, 1, 50), (1, 1, 175), (1, 2, 125), (2, 2, 150), (2, 3, 250)]
        expected_Z = 12200

        self.assertTrue(set(expected_X) == set(sol))
        self.assertEqual(expected_Z, z)

    def testCaseVogel1(self):
        _costs = np.array([[2, 3, 4, 2, 4],
                           [8, 4, 1, 4, 1],
                           [9, 7, 3, 7, 2]])
        _demand = np.array([60, 70, 120, 130, 100])
        _supply = np.array([140, 180, 160])

        x, z = north_west(_costs, _demand, _supply)
        expected_X = [(0, 0, 60), (0, 1, 70), (0, 2, 10), (1, 2, 110), (1, 3, 70), (2, 3, 60), (2, 4, 100)]
        expected_Z = 1380
        self.assertTrue(set(expected_X) == set(x))
        self.assertEqual(expected_Z, z)

    def testCaseVogel2(self):
        costs = np.array([[10, 8, 7, 26],
                          [11, 5, 2, 13],
                          [20, 5, 1, 15]])
        demand = np.array([50, 50, 50, 50])
        supply = np.array([100, 75, 25])
        expected_X = [(2, 2, 25), (1, 3, 50), (1, 2, 25), (0, 1, 50), (0, 0, 50)]
        expected_Z = 1625

        x, z = vogel(costs, demand, supply)
        self.assertTrue(set(expected_X) == set(x))
        self.assertEqual(expected_Z, z)

    def testCaseVogel3(self):
        # https://byjus.com/maths/vogels-approximation-method/
        costs = np.array([[3, 2, 7, 6],
                         [7, 5, 2, 3],
                         [2, 5, 4, 5]])
        demand = np.array([60, 40, 20, 15])
        supply = np.array([50, 60, 25])
        expected_X = [(0, 1, 40), (0, 0, 10), (2, 0, 25), (1, 2, 20), (1, 3, 15), (1, 0, 25)]
        expected_Z = 420

        x, z = vogel(costs, demand, supply)
        self.assertTrue(set(expected_X) == set(x))
        self.assertEqual(expected_Z, z)

    def testCaseRussell1(self):
        # https://cbom.atozmath.com/example/CBOM/Transportation.aspx?q=ram&q1=E1
        costs = np.array([[19, 30, 50, 10],
                          [70, 30, 40, 60],
                          [40, 8, 70, 20]])
        demand = np.array([5, 8, 7, 14])
        supply = np.array([7, 9, 18])

        expected_X = [(0, 0, 5), (0, 1, 2), (1, 1, 2), (1, 2, 7), (2, 1, 4), (2, 3, 14)]
        expected_Z = 807

        x, z = russell(costs, demand, supply)
        self.assertTrue(set(expected_X) == set(x))
        self.assertEqual(expected_Z, z)

    def testCaseRussell2(self):
        costs = np.array([[20, 10, 15, 50, 10],
                          [1,  30, 10, 25, 5],
                          [5,  10, 15, 20, 2],
                          [15, 20, 10, 25, 5]])
        demand = np.array([20, 10, 20, 10, 40])
        supply = np.array([10, 30, 20, 40])
        expected_X = [(0, 1, 10), (1, 0, 20), (1, 2, 10), (3, 2, 10), (2, 3, 10), (2, 4, 10), (3, 4, 30)]
        expected_Z = 690

        x, z = russell(costs, demand, supply)
        self.assertTrue(set(expected_X) == set(x))
        self.assertEqual(expected_Z, z)

    def testCaseRussel3(self):
        costs = np.array([[3, 2, 7, 6],
                          [7, 5, 2, 3],
                          [2, 5, 4, 5]])
        demand = np.array([60, 40, 20, 15])
        supply = np.array([50, 60, 25])
        expected_X = [(1, 2, 20), (0, 0, 50), (2, 0, 10), (1, 3, 15), (1, 1, 25), (2, 1, 15)]
        expected_Z = 455

        x, z = russell(costs, demand, supply)
        self.assertTrue(set(expected_X) == set(x))
        self.assertEqual(expected_Z, z)


def run_tests():
    unittest.main()


if __name__ == '__main__':
    unittest.main()
