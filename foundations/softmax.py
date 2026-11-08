import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        maxelement = max(z)

        totalsum = 0
        for i in range (len(z)):
            totalsum += np.exp (z[i] - maxelement)
        
        softmax = []
        for i in range (len(z)):
            softmax.append( np.exp (z[i] - maxelement) / (totalsum))

        return np.round (softmax, 4)
            

