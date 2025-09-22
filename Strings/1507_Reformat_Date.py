"""
1507. Reformat Date
Level: Easy
Topics: String
Link: https://leetcode.com/problems/reformat-date?envType=problem-list-v2&envId=string
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        stack = []
        res = ''
        word = ''
        date += ' '
        monthMap = {"Jan" : '01', "Feb" : '02', "Mar" : '03', "Apr" : '04', "May" : '05', "Jun" : '06', "Jul" : '07', "Aug" : '08', "Sep" : '09', "Oct" : '10', "Nov" : '11', "Dec" : '12'}
        for c in date:
            if c == ' ':
                stack.append(word)
                word = ''
                continue
            word += c
        year = stack.pop()
        month = stack.pop()
        date = stack.pop()
        month = monthMap[month]
        if len(date) < 4:
            date = '0' + date[0: 1]
        else:
            date = date[0: 2]
        res = year + "-" + month + "-" + date
        return res