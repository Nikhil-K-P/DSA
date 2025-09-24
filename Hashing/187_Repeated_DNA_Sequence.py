"""
187. Repeated DNA Sequences
Level: Medium
Topic: Hashing, String, Sliding Window
Link: https://leetcode.com/problems/repeated-dna-sequences?envType=problem-list-v2&envId=hash-table
Time Complexity: O(n) n - len(s)
Space Complexity: O(n)
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequence = {}
        res = []
        i, j = 0, 9
        while j < len(s):
            DNA = s[i : j + 1]
            sequence[DNA] = 1 + sequence.get(DNA, 0)
            i += 1
            j += 1
        for key, val in sequence.items():
            if val > 1:
                res.append(key)
        return res