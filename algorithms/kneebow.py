import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


class Rotor:

    def __init__(self):
        """
        Rotor. Find the elbow or knee of a 2d array.

        The algorithm rotates the curve so that the slope from min to max is zero. Subsequently, it takes the min value
        for the elbow or the max value for the knee.

        """
        self._data = None
        self._scale = None
        self._scaler = None
        self._theta = None

    def fit_rotate(self, data, scale=True, theta=None):
        """
        Take a 2d array, scale it and rotate it so that the slope from min to max is zero.

        :param data:    2d numpy array. The data to rotate.
        :param scale:   boolean. True if data should be scaled before rotation (highly recommended)
        :param theta:   float or None. Angle of rotation in radians. If None the angle is calculated from min & max
        """
        self._data = data
        self._scale = scale
        self._theta = theta
        if scale:
            self._scaler = MinMaxScaler()
            self._data = self._scaler.fit_transform(self._data)
        if theta is not None:
            self._theta = theta
        else:
            self._set_theta_auto()
        self._data = self.rotate_vector(self._data, self._theta)

    def get_elbow_index(self):
        """
        Return the index of the elbow of the curve.

        :return:  integer. Index of the elbow.
        """
        return np.where(self._data == self._data.min())[0][0]

    def get_knee_index(self):
        """
        Return the index of the knee of the curve.

        :return:  integer. Index of the knee.
        """
        return np.where(self._data == self._data.max())[0][0]

    def plot_elbow(self):
        """
        Plot the data points together with a line that marks the elbow.
        """
        data = self.rotate_vector(self._data, -self._theta)
        if self._scale:
            data = self._scaler.inverse_transform(data)
        elb_idx = self.get_elbow_index()
        plt.scatter(data[:, 0], data[:, 1])
        plt.vlines(data[elb_idx, 0], ymin=data[:, 1].min(), ymax=data[:, 1].max(), colors='red', linestyles='--')

    def plot_knee(self):
        """
        Plot the data points together with a line that marks the knee.
        """
        data = self.rotate_vector(self._data, -self._theta)
        if self._scale:
            data = self._scaler.inverse_transform(data)
        elb_idx = self.get_knee_index()
        plt.scatter(data[:, 0], data[:, 1])
        plt.vlines(data[elb_idx, 0], ymin=data[:, 1].min(), ymax=data[:, 1].max(), colors='red', linestyles='--')

    def _set_theta_auto(self):
        """
        Set theta to the radiant of the slope from the first to last value of the data.
        """
        self._theta = np.arctan2(self._data[-1, 1] - self._data[0, 1],
                                 self._data[-1, 0] - self._data[0, 0])

    @staticmethod
    def rotate_vector(data, theta):
        """
        Rotate a 2d vector.

        :param data:    2d numpy array. The data that should be rotated.
        :param theta:   float. The angle of rotation in radians.
        :return:        2d numpy array. The rotated data.
        """
        # make rotation matrix
        co = np.cos(theta)
        si = np.sin(theta)
        rotation_matrix = np.array(((co, -si), (si, co)))
        # rotate data vector
        return data.dot(rotation_matrix)
