"""
819. Most Common Word
Level: Easy
Topics: Hash Table, String
Link: https://leetcode.com/problems/most-common-word?envType=problem-list-v2&envId=hash-table
Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        bannedSet = set(banned)
        wordMap = {}
        maxCount = 0
        res = ""
        word = ""
        paragraph += " "
        for c in paragraph:
            if c.isalnum():
                word += c.lower()
            else:
                if word and word not in bannedSet:
                    wordMap[word] = 1 + wordMap.get(word, 0)
                    if wordMap[word] > maxCount:
                        maxCount = wordMap[word]
                        res = word
                word = ""
        return res