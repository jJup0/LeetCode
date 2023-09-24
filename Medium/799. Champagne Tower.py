class Solution:
    """
    We stack glasses in a pyramid, where the first row has 1 glass, the second
    row has 2 glasses, and so on until the 100th row.  Each glass holds one cup
    of champagne.

    Then, some champagne is poured into the first glass at the top.  When the
    topmost glass is full, any excess liquid poured will fall equally to the
    glass immediately to the left and right of it.  When those glasses become
    full, any excess champagne will fall equally to the left and right of those
    glasses, and so on.  (A glass at the bottom row has its excess champagne
    fall on the floor.)

    For example, after one cup of champagne is poured, the top most glass is full.
    After two cups of champagne are poured, the two glasses on the second row are
    half full.  After three cups of champagne are poured, those two cups become
    full - there are 3 full glasses total now.  After four cups of champagne are
    poured, the third row has the middle glass half full, and the two outside
    glasses are a quarter full, as pictured below.

    Constraints:
    - 0 <= poured <= 10^9
    - 0 <= query_glass <= query_row < 100
    """

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # base case
        if query_row == 0:
            return min(1.0, poured)

        glasses: list[float] = [poured]  # stores champagne supply of glasses
        for row_nr in range(1, query_row + 1):
            # use only one working array; at each new row one glass added to the end
            glasses.append(0)
            # glasses from previous row at index i pour into current row at indexes i and i+1
            # go through previous glasses row from last to first and pour overflowing champagne
            for i in range(row_nr - 1, -1, -1):
                # if glass is not overflowing, nothing to pour, continue
                if glasses[i] < 1:
                    glasses[i] = 0
                    continue
                # one unit of champagne "kept" in glass above, half is poured to each glass underneath
                glasses[i] = (glasses[i] - 1) / 2
                # pour other half to i+1
                glasses[i + 1] += glasses[i]

        # max capacity of glass is 1
        return min(1.0, glasses[query_glass])
