"""
1629. Slowest Key
Level: Easy
Topics: Array, String
Link: https://leetcode.com/problems/slowest-key?envType=problem-list-v2&envId=string
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        duration = [0] * 26
        start = 0
        for i in range(n):
            end = releaseTimes[i]
            time = end - start 
            character = keysPressed[i]
            duration[ord(character) - ord('a')] = max(duration[ord(character) - ord('a')], time)
            start = end
        
        res = 0
        maxTime = 0 
        print(duration)
        for i in range(25, -1, -1):
            if duration[i] > maxTime:
                res = i 
                maxTime = duration[i]
        res = chr(res + 97)
        return res