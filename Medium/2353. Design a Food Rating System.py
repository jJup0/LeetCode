import heapq
from collections import defaultdict


class FoodRatings(object):
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        """
        O(n) / O(n)     time / space complexity
        """
        # keep a max heap of foods for each type of cuisine
        self.cuisine_to_heap: defaultdict[str, list[tuple[int, str]]] = defaultdict(
            list
        )
        self.food_to_cuisine: dict[str, str] = {}
        self.food_to_rating: dict[str, int] = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            # store negated rating, to easily compare to rating on the heap
            self.food_to_rating[f] = -r
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))

    def changeRating(self, food: str, new_rating: int) -> None:
        """
        O(1) time complexity
        """
        cuisine = self.food_to_cuisine[food]
        # only push to heap, stale data will be removed in highestRated()
        heapq.heappush(self.cuisine_to_heap[cuisine], (-new_rating, food))
        self.food_to_rating[food] = -new_rating

    def highestRated(self, cuisine: str) -> str:
        """
        Total time complexity of all calls to highestRated() = O(calls to changeRating())
        """
        cuisine_heap = self.cuisine_to_heap[cuisine]
        while True:
            highest_rating, highest_rated_food = cuisine_heap[0]
            # check if the rating of the item is the current rating
            if highest_rating != self.food_to_rating[highest_rated_food]:
                # if not, remove the item from the heap
                heapq.heappop(cuisine_heap)
            else:
                # else return the name of the food
                return highest_rated_food
