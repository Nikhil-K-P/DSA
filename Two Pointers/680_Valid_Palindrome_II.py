"""
824. Goat Latin
Level: Easy
Topic: String
Link: https://leetcode.com/problems/valid-palindrome-ii?envType=problem-list-v2&envId=two-pointers
Time Complexity: O(n) n - no of characters in sentence
Space Complexity: O(n)
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True 
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
            l += 1
            r -= 1
        return True 