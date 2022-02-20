class BinaryMatrix(object):
    def get(self, x: int, y: int) -> int:
        pass

    def dimensions(self) -> []:
        pass


class mySolution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        rowsStillAlive,  previousAlive = list(range(0, rows)), list(range(0, rows))
        prevMid, mid = cols,  cols//2
        while rowsStillAlive:
            i = 0
            while i < len(rowsStillAlive):
                if not(binaryMatrix.get(rowsStillAlive[i], mid)):
                    del rowsStillAlive[i]
                else:
                    i += 1
            if not(rowsStillAlive):
                if mid >= cols-1:
                    return -1
                else:
                    if prevMid - 1 == mid:
                        return prevMid
                    rowsStillAlive = previousAlive.copy()
                    mid = (mid+prevMid)//2
            else:
                if mid == 0:
                    return 0
                prevMid = mid
                mid = mid//2
                previousAlive = rowsStillAlive.copy()


class hint2Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        curCoord = [0, cols-1]
        while curCoord[0] < rows:
            if binaryMatrix.get(curCoord[0], curCoord[1]):
                curCoord[1] -= 1
            else:
                curCoord[0] += 1
            if curCoord[1] == -1:
                return 0
        if curCoord[1] == cols-1:
            return -1
        return curCoord[1] + 1
