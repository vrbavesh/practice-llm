class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        derx = 2 * x
        
        for i in range(iterations):
            x = x - learning_rate * derx
            derx = 2 * x

        return round (x, 5)  
        
