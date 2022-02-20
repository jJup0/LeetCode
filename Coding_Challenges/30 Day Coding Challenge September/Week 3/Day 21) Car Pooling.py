class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1000
        for passengers, start, end in trips:
            timestamp[start] += passengers
            timestamp[end] -= passengers

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False
        return True

    # def carPooling(trips: List[List[int]], capacity: int) -> bool:
    #     trips.sort(key=lambda x: x[1])
    #     queue = []
    #     currPassengers = 0
    #     for passengers, start, end in trips:
    #         while queue and queue[0][0] <= start:
    #             currPassengers -= queue.pop(0)[1]
    #         insort(queue, (end, passengers))
    #         currPassengers += passengers
    #         if currPassengers > capacity:
    #             return False
    #     return True
