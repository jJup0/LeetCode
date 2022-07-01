from typing import List


class Solution:
    """
    You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes,
    where boxTypes[i] = [numberOfBoxes_i, numberOfUnitsPerBox_i]:
        numberOfBoxes_i is the number of boxes of type i.
        numberOfUnitsPerBoxi is the number of units in each box of the type i.
    You are also given an integer truckSize, which is the maximum number of boxes that can be put on
    the truck. You can choose any boxes to put on the truck as long as the number of boxes does not
    exceed truckSize.
    Return the maximum total number of units that can be put on the truck.
    Constraints:
        1 <= boxTypes.length <= 1000
        1 <= numberOfBoxes_i, numberOfUnitsPerBox_i <= 1000
        1 <= truckSize <= 10^6
    """

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # result variable
        res = 0

        # sort boxes, with unit amount descending, so boxes with most units can greedily be taken
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        for boxes, units in boxTypes:
            # if more than enough space is still availible, add all boxes to truck
            if boxes < truckSize:
                res += boxes * units
                truckSize -= boxes
            else:
                # otherwise add remaining space of boxes and break
                res += truckSize * units
                break

        return res
