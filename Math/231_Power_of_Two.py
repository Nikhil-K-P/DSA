"""
231. Power of Two
Level: Easy
Topics: Math, Bit Manipulation
Link: 
Time Complexion: O(log n)
Space Complexion: O(1)
Note: 
Other Approches: 

"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False 
        count = 0
        while n:
            rem = n % 2
            if rem: 
                count += 1
            n = n // 2
        return count <= 1
    
    
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0