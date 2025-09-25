"""
824. Goat Latin
Level: Easy
Topic: String
Link: https://leetcode.com/problems/goat-latin
Time Complexity: O(n) n - no of characters in sentence
Space Complexity: O(n)
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = ''
        word = ''
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        sentence += ' '
        for s in sentence:
            if s == ' ':
                count += 1
                
                if word[0].lower() in vowels:
                    res += word 
                else:
                    res += word[1 :] + word[0] 
                
                res = res + 'ma' + 'a' * count + ' '
                word = ''
                continue 
            word += s
        return res.strip()