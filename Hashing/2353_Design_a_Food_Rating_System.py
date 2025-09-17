"""
2353. Design a Food Rating System
Level: Medium
Topics: Hash Table, Design, Sorted Set, Priority Queue
Link: https://leetcode.com/problems/design-a-food-rating-system?envType=daily-question&envId=2025-09-17
Time Complexity: O(log N) for changeRating and O(1) for highestRated
Space Complexity: O(N)
"""

from collections import defaultdict
from sortedcontainers import SortedSet


class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        n = len(cuisines)
        self.foodMap = {}
        self.cuisineMap = {}
        self.topRating = defaultdict(SortedSet)
        for i in range(n):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            self.foodMap[food] = rating 
            self.cuisineMap[food] = cuisine
            self.topRating[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        ratingOld = self.foodMap[food]
        cuisine = self.cuisineMap[food]
        self.topRating[cuisine].remove((- ratingOld, food))
        self.foodMap[food] = newRating 
        self.topRating[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.topRating[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)