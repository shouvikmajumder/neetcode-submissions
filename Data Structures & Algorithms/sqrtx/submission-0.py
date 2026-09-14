import math
class Solution:
    def mySqrt(self, x: int) -> int:
        max_valid = 0

        left, right = 0, x

        while left <= right: 
            mp = (left + right) // 2 
            if (mp **2) == x:
                return mp
            elif (mp ** 2) > x:
                right = mp -1 
            elif  (mp ** 2) < x:
                left = mp + 1

        return right