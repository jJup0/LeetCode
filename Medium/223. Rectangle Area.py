class Solution:
    """
    Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
    The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
    The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).
    Constraints:
        -10^4 <= ax1 <= ax2 <= 10^4
        -10^4 <= ay1 <= ay2 <= 10^4
        -10^4 <= bx1 <= bx2 <= 10^4
        -10^4 <= by1 <= by2 <= 10^4
    """

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # calculate area of two rectangles like normal
        area1 = (ax2 - ax1) * (ay2-ay1)
        area2 = (bx2 - bx1) * (by2-by1)

        # calculate coordinates for overlap rectangle
        # starting coordinates are left-most, lower-most coordinates shared by both rectangles, so take max
        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)

        # starting coordinates are right-most, upper-most coordinates shared by both rectangles, so take min
        cx2 = min(ax2, bx2)
        cy2 = min(ay2, by2)

        # calculate area of over lap, default a side length to 0 if negative
        # (has to be done for both otherwise negative * negative = postive)
        overlap = max(0, (cx2 - cx1)) * max(0, (cy2 - cy1))

        # add areas of rectangles and subtract overlap
        return area1 + area2 - overlap
