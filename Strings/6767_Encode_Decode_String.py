"""
6767. Encode and Decode Strings
Level: Medium
Topic: Strings
Link: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ''
        for s in strs:
            n = len(s)
            res = res + str(n) + "#" + s
        return res


    def decode(self, s: str) -> list[str]:
        res = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] != "#":
                j += 1
            length = int(s[i : j])
            i = j + 1
            j = i + length 
            word = s[i : j]
            res.append(word)
            i = j 
        return res
