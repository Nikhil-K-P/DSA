"""
125. Valid Palindrome
Level: Easy
Topics: Two Pointers, String
Link: https://leetcode.com/problems/valid-palindrome
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
                continue 
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True 