"""
438. Find All Anagrams in a String
Level: Medium
Topic: Hashing, String, Sliding Window
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string?envType=problem-list-v2&envId=hash-table
Time Complexity: O(n) 
Space Complexity: O(1)
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        pMap = [0] * 26
        for c in p:
            pMap[ord(c) - ord('a')] += 1 
        n, m = len(p), len(s)
        i, j = 0, n
        sMap = [0] * 26

        for c in s[i : j]:
            sMap[ord(c) - ord('a')] += 1

        for j in range(n, m):
            if sMap == pMap:
                res.append(i)
            sMap[ord(s[j]) - ord('a')] += 1 
            sMap[ord(s[i]) - ord('a')] -= 1 
            i += 1
        
        if sMap == pMap:
            res.append(i)
            
        return res