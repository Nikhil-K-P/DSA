"""
3005. Count Elements With Maximum Frequency
Level: Easy 
Topics: Arrays, Hash Table, Counting
Link: https://leetcode.com/problems/count-elements-with-maximum-frequency?envType=daily-question&envId=2025-09-22
Time Complexity: O(n)
Space Complexity: O(n)
Note: Can also be solved in single pass 
"""


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        count = 0
        frequency = {}
        maxCount = 0
        for n in nums:
            frequency[n] = 1 + frequency.get(n, 0)
            maxCount = max(maxCount, frequency[n])
            
        for num, cnt in frequency.items():
            if cnt == maxCount:
                count += 1
        
        return maxCount * count
    

class Solution:
    def maxFrequencyElement(self, nums: list[int]) -> int:
        count = {}
        maxFrequency = 0 
        total_frequency = 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            frequency = count[n]

            if frequency > maxFrequency:
                maxFrequency = frequency
                total_frequency = frequency
            elif frequency == maxFrequency:
                total_frequency += frequency
        return total_frequency