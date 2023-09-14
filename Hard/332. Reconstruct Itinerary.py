from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # create adjacency lists with count
        flights_from: dict[str, dict[str, int]] = defaultdict(dict)
        for a, b in tickets:
            if b not in flights_from[a]:
                flights_from[a][b] = 0
            flights_from[a][b] += 1

        res_in_reverse: list[str] = []

        def dfs(curr_airport: str, flights_remaining: int):
            """
            DFS visit aiports until a valid itenerary is found,
            returns true if a valid flight itenerary has been found.
            """
            if flights_remaining == 0:
                # all flights have been taken, add current airport to result list
                res_in_reverse.append(curr_airport)
                return True

            destinations = flights_from[curr_airport]
            # iterate through destinations in alphabetical order
            for dest in sorted(destinations):
                flight_count = destinations[dest]
                if flight_count == 1:
                    # if only one flight remaining to destination,
                    # pop it from adjacency list
                    destinations.pop(dest)
                    if dfs(dest, flights_remaining - 1):
                        # if a valid itinerary was found using this flight,
                        # append current airport to end of list
                        res_in_reverse.append(curr_airport)
                        return True
                    # reset the flight to use for later/different flight order
                    destinations[dest] = 1
                else:
                    # same procedure as above, without popping
                    destinations[dest] -= 1
                    if dfs(dest, flights_remaining - 1):
                        res_in_reverse.append(curr_airport)
                        return True
                    destinations[dest] += 1

        # dfs and start at JFK
        dfs("JFK", len(tickets))

        # "undo" reverse order
        return res_in_reverse[::-1]

    def findItinerary_magic(self, tickets: list[list[str]]) -> list[str]:
        """
        O(n * log(n)) / O(n)    time / space complexity
        """
        adj_list: defaultdict[str, list[str]] = defaultdict(list)
        res: list[str] = []

        for departure, arrival in tickets:
            adj_list[departure].append(arrival)

        for key in adj_list:
            adj_list[key].sort(reverse=True)

        def dfs(airport: str):
            # this magically appends airports in the right order
            # technically just backtracking the dfs traversal but still, I have
            # do not have a firm grasp on why this obviously works
            while adj_list[airport]:
                dfs(adj_list[airport].pop())
            res.append(airport)

        dfs("JFK")
        return res[::-1]
