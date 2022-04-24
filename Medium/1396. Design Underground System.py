class UndergroundSystem:

    def __init__(self):
        # mapping of trip to total travel time over all trips and total trips
        # storing integers allows exact calculation of getAverageTime in O(1)
        self.totaltime_and_trips = {}
        # mapping of id to check-in time
        self.check_ins = {}

    def checkIn(self, id: int, station_name: str, t: int) -> None:
        # store check-in station and time
        self.check_ins[id] = (station_name, t)

    def checkOut(self, id: int, end_station: str, t_end: int) -> None:
        # get starting station and time from id
        start_station, t_start = self.check_ins.pop(id)

        trip = (start_station, end_station)
        # if trip already exists, update total time and total trips
        if trip in self.totaltime_and_trips:
            prev_total_time_and_trips = self.totaltime_and_trips[trip]
            prev_total_time_and_trips[0] += t_end - t_start
            prev_total_time_and_trips[1] += 1
        else:
            # otherwise initialize list of fixed length = 2 with travel time and 1
            self.totaltime_and_trips[trip] = [t_end - t_start, 1]

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        # average_time = total_time / trips_taken
        totaltime_and_trips = self.totaltime_and_trips[(start_station, end_station)]
        return totaltime_and_trips[0]/totaltime_and_trips[1]
