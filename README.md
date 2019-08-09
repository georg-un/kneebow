# kneebow

Find the knee of a curve or the elbow of a curve.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3baba89ac29b4a96bd990148deb36236)](https://www.codacy.com/app/georg-un/kneebow?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=georg-un/kneebow&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/georg-un/kneebow.svg?branch=master)](https://travis-ci.org/georg-un/kneebow)
[![codecov](https://codecov.io/gh/georg-un/kneebow/branch/master/graph/badge.svg)](https://codecov.io/gh/georg-un/kneebow)

## How it works

kneebow builds upon a very simple idea: if we want to find the elbow of a curve, we can simply rotate the data so that curve looks down and then take the minimum value. If we want to find the knee of the curve, we take the maximum value instead. It's as simple as that.

## Installation

You can install the package via pip:

```sh
pip install kneebow
```

Alternatively, you can also install the latest version from GitHub:

```sh
pip install git+https://github.com/georg-un/kneebow.git
```

## Usage

Let's assume, we try to find the elbow of the following data:

```python
import numpy as np
data = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8],  # linear until (8,8)
                 [9, 16], [10, 32], [11, 64], [12, 128], [13, 256], [14, 512]])   # exponential afterwards
```
Let's have a peak how this data looks like:

![data_plot](https://raw.githubusercontent.com/georg-un/kneebow/master/assets/data_plot.png)

To find the elbow, we create an instance of the `Rotor` class and use its `fit_rotate` method:

```python
from kneebow.rotor import Rotor
 
rotor = Rotor()
rotor.fit_rotate(data)
```
Now we can get the index of the elbow as follows:
```python
elbow_idx = rotor.get_elbow_index()
print(elbow_idx)  # 11
```
The `Rotor` class also comes with plot methods to inspect the data visually together with the estimated elbow/knee:
```python
rotor.plot_elbow()
```
![rotor_plot](https://raw.githubusercontent.com/georg-un/kneebow/master/assets/rotor_plot.png)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.