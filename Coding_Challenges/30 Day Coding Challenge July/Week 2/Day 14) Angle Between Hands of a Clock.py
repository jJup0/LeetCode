class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteangle = minutes*6
        hourangle = hour*30+minutes/2
        dif = abs(minuteangle - hourangle)
        return dif if dif < 180 else 360 - dif
