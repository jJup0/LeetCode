class Solution:
    """
    We have n buildings numbered from 0 to n - 1. Each building has a number of
    employees. It's transfer season, and some employees want to change the building they
    reside in.

    You are given an array requests where requests[i] = [from_i, to_i] represents an
    employee's request to transfer from building from_i to building to_i.

    All buildings are full, so a list of requests is achievable only if for each
    building, the net change in employee transfers is zero. This means the number of
    employees leaving is equal to the number of employees moving in. For example if n = 3
    and two employees are leaving building 0, one is leaving building 1, and one is
    leaving building 2, there should be two employees moving to building 0, one employee
    moving to building 1, and one employee moving to building 2.

    Return the maximum number of achievable requests.

    Constraints:
    - 1 <= n <= 20
    - 1 <= requests.length <= 16
    - requests[i].length == 2
    - 0 <= from_i, to_i < n
    """

    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        def try_all_transfers(
            curr_request_index: int, building_space_diff: list[int], curr_transfers: int
        ) -> int:
            """Combinatorically try each way of performing transfer requests.

            O(2^requests) / O(requests)     time / space complexity
            Args:
                curr_request_index (int):
                  Index of requests, for which request is to be handled next.
                building_space_diff (list[int]):
                  Space difference in buildings. [1, -3] would mean that building "0"
                  has 1 employee to many and building "1" 3 employees to few.
                curr_transfers (int): _description_

            Returns:
                int: Best transfer count
            """
            nonlocal requests

            # if no more transfers left ...
            if curr_request_index == len(requests):
                # ... and no buildings are overfilled
                if all(diff == 0 for diff in building_space_diff):
                    # return current transfer count
                    return curr_transfers
                # else none of the transfers "made" so far can actually be made
                return 0

            ### do current transfer
            a, b = requests[curr_request_index]
            # change state
            building_space_diff[a] -= 1
            building_space_diff[b] += 1
            result = try_all_transfers(
                curr_request_index + 1, building_space_diff, curr_transfers + 1
            )
            # revert back to original state
            building_space_diff[a] += 1
            building_space_diff[b] -= 1

            ### dont do transfer
            result = max(
                result,
                try_all_transfers(
                    curr_request_index + 1, building_space_diff, curr_transfers
                ),
            )
            return result

        requests, self_transfers = self._preprocess_requests(n, requests)
        return try_all_transfers(0, [0] * n, 0) + self_transfers

    def _preprocess_requests(self, n: int, requests: list[list[int]]):
        """Prepocesses requests, reducing the amount of requests to consider.

        Removes buildings that are sources or sinks (building with no transfer
        requests to and from that building), and requests for staying in the
        current building.
        O(requests + n) / O(requests)     time / space complexity
        Args:
            n (int):
              The amount of buildings that exist.
            requests (list[list[int]]):
              The transfer requests given as [a,b] such that a person
              wants to transfer from building a to building b.

        Returns:
            tuple[list[int], int]:
              A pair of values, the first being the new and reduced requests list,
              the second being the amount of self transfers.
        """
        self_transfers = 0
        # track buildings that employees want to transfer to or from
        transfer_from: list[list[int]] = [[] for _ in range(n)]
        transfer_to: list[list[int]] = [[] for _ in range(n)]

        for transfer in requests:
            a, b = transfer
            if a == b:
                self_transfers += 1
            else:
                transfer_from[a].append(b)
                transfer_to[b].append(a)

        # buildings remaining, which are neither sinks or sources
        buildings_remaining = set(range(n))

        # remove sinks and sources
        sinks_or_sources_removed = True
        while sinks_or_sources_removed:
            sinks_or_sources_removed = False
            for building in tuple(buildings_remaining):
                is_sink_or_source = False
                if not transfer_from[building]:
                    # building is sink
                    is_sink_or_source = True
                    # removed transfers to this building
                    for source_building in transfer_to[building]:
                        transfer_from[source_building] = [
                            b for b in transfer_from[source_building] if b != building
                        ]

                elif not transfer_to[building]:
                    # building is source
                    is_sink_or_source = True
                    # removed transfers from this building
                    for source_building in transfer_from[building]:
                        transfer_to[source_building] = [
                            b for b in transfer_to[source_building] if b != building
                        ]

                if is_sink_or_source:
                    # building is sink or source, remove all transfers from and to this building
                    transfer_to[building].clear()
                    transfer_from[building].clear()
                    buildings_remaining.remove(building)
                    sinks_or_sources_removed = True

        # construct new requests lists
        new_requests: list[list[int]] = []
        for a, bs in enumerate(transfer_from):
            for b in bs:
                new_requests.append([a, b])

        return new_requests, self_transfers
