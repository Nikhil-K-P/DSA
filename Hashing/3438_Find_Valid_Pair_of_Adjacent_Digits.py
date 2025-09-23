"""
3438. Find Valid Pair of Adjacent Digits
Level: Easy
Topics: Hashing, String, Counting
Link: https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string?envType=problem-list-v2&envId=counting
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def findValidPair(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        n = len(s)
        for i in range(n - 1):
            c1, c2 = s[i], s[i + 1]
            if c1 == c2:
                continue 
            else:
                if count[c1] == int(c1) and count[c2] == int(c2):
                    return c1 + c2
        return ""
