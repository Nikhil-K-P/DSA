"""
929. Unique Email Addresses
Level: Easy
Topic: Array, Hashing, String
Link: https://leetcode.com/problems/unique-email-addresses?envType=problem-list-v2&envId=hash-table
Time Complexity: O(n * m) n - len(emails), m - avg len(email)
Space Complexity: O(n)
"""


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        mailSet = set()
        for email in emails:
            index = email.index('@')
            localName = email[ : index]
            domainName = email[index + 1 : ]
            buffer = ''
            for c in localName:
                if c == '+':
                    break
                elif c == '.':
                    continue 
                else:
                    buffer += c
            localName = buffer
            validEmail = localName + '@' + domainName
            mailSet.add(validEmail)
        return len(mailSet)