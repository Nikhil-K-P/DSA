"""
2085. Count Common Words With One Occurrence
Level: Easy
Topic: Array, Hash Table, String, Counting
Link: https://leetcode.com/problems/count-common-words-with-one-occurrence?envType=problem-list-v2&envId=hash-table
Time Complexity: O(n + m) n - len(words1), m - len(words2)
Space Complexity: O(n + m)
"""


class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        res = 0
        count1, count2 = {}, {}
        for word in words1:
            count1[word] = 1 + count1.get(word, 0)
        for word in words2:
            count2[word] = 1 + count2.get(word, 0)
        print(count1)
        print(count2)
        for key, value in count1.items():
            if value == 1:
                if key in count2 and count2[key] == 1:
                    res += 1
        return res 