"""
1912. Design Movie Rental System
Level: Hard
Topics: Array, Hash Table, Design, Heap (Priority Queue), Ordered Set
Link: https://leetcode.com/problems/design-movie-rental-system?envType=daily-question&envId=2025-09-21
Time Complexity: O(log n)
Space Complexity: O(m), m - number of entries
"""


from collections import defaultdict
from sortedcontainers import SortedSet


class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]):
        self.movieInfo = {}
        self.unrentedMovie = defaultdict(SortedSet)
        self.rentedMovie = SortedSet()
        for movie in entries:
            shop, movie, price = movie 
            self.movieInfo[((movie, shop))] = price
            self.unrentedMovie[movie].add((price, shop))
        
    def search(self, movie: int) -> list[int]:
        if movie not in self.unrentedMovie:
            return []
        n = len(self.unrentedMovie[movie])
        values = self.unrentedMovie[movie]
        if n < 5:
            return [shop for price, shop in values]
        res = []
        for price, shop in values:
            res.append(shop)
            if len(res) == 5:
                return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.movieInfo[(movie, shop)]
        self.unrentedMovie[movie].remove((price, shop))
        self.rentedMovie.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.movieInfo[(movie, shop)]
        self.rentedMovie.remove((price, shop, movie))
        self.unrentedMovie[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        if len(self.rentedMovie) < 5:
            return [[shop, movie] for price, shop, movie in self.rentedMovie]
        res = []
        for price, shop, movie in self.rentedMovie:
            res.append([shop, movie])
            if len(res) == 5:
                return res
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()