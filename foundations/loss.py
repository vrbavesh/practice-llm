import numpy as np
import math
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
    
        y_pred = np.clip(y_pred, 1e-7, 1 - 1e-7)
        n = len(y_true)
        calc = 0
        for i in range(n):
            calc += (y_true[i] * math.log(y_pred[i]) + (1 - y_true[i]) * math.log(1 - y_pred[i]))

        loss = -1 / n * calc

        return round(float(loss), 4)
            

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:

        y_pred = np.clip(y_pred, 1e-7, 1 - 1e-7)
        n = len(y_true)
        num_classes = len(y_true[0])
        
        calc = 0

        for i in range(n):
            for c in range(num_classes):
                calc += y_true[i][c] * math.log(y_pred[i][c])

        loss = -1 / n * calc

        return round(float(loss), 4)