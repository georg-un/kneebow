import unittest
import numpy as np

from kneebow.rotor import Rotor


sample_inc = np.array([
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 7],
    [8, 8],
    [9, 16],
    [10, 32],
    [11, 64],
    [12, 128],
    [13, 256],
    [14, 512]
])

sample_dec = np.array([
    [1, 50],
    [2, 49],
    [3, 47],
    [4, 46],
    [5, 49],
    [6, 42],
    [7, 30],
    [8, 20],
    [9, -10],
    [10, -50],
    [11, -100],
    [12, -105],
    [13, -108],
])


class TestRotor(unittest.TestCase):

    def test_initialization(self):
        r = Rotor()
        self.assertIsNotNone(r)

    def test_fit_rotate_default_parameter(self):
        r = Rotor()
        r.fit_rotate(sample_inc)
        self.assertTrue(r._scale)
        self.assertIsNotNone(r._theta)

    def test_fit_rotate(self):
        r = Rotor()
        r.fit_rotate(sample_inc)
        self.assertIsNotNone(r._data)

    def test_scaling(self):
        r = Rotor()
        r.fit_rotate(sample_inc, scale=True, theta=0)
        self.assertLessEqual(r._data[:, 0].max(), 1.00000001)
        self.assertLessEqual(r._data[:, 1].max(), 1.00000001)
        self.assertGreaterEqual(r._data[:, 0].min(), -0.00000001)
        self.assertGreaterEqual(r._data[:, 1].min(), -0.00000001)

    def test_fit_rotate_params(self):
        r = Rotor()
        r.fit_rotate(sample_inc, scale=False, theta=0.7)
        self.assertFalse(r._scale)
        self.assertEqual(r._theta, 0.7)

    def test_rotation(self):
        data = np.array([[0, 0], [1, 0], [0, 1]])
        r = Rotor()
        r.fit_rotate(data, scale=False, theta=np.radians(45))
        self.assertAlmostEqual(r._data[0].tolist()[0], 0, delta=0.01)
        self.assertAlmostEqual(r._data[0].tolist()[1], 0, delta=0.01)
        self.assertAlmostEqual(r._data[1].tolist()[0], 0.71, delta=0.01)
        self.assertAlmostEqual(r._data[1].tolist()[1], -0.71, delta=0.01)
        self.assertAlmostEqual(r._data[2].tolist()[0], 0.71, delta=0.01)
        self.assertAlmostEqual(r._data[2].tolist()[1], 0.71, delta=0.01)

    def test_detect_elbow(self):
        r = Rotor()
        r.fit_rotate(sample_inc)
        self.assertAlmostEqual(r.get_elbow_index(), 11, delta=1)

    def test_detect_knee(self):
        r = Rotor()
        r.fit_rotate(sample_dec)
        self.assertAlmostEqual(r.get_knee_index(), 7, delta=1)


if __name__ == '__main__':
    unittest.main()
