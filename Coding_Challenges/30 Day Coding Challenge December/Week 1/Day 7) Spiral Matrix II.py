class originalSolution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        res = [[0]*n for _ in range(n)]
        curr = 1
        for ring in range((n//2)+1):  # amount of "rings" the matrix has
            y = ring
            for x in range(ring, n-ring):  # top row
                res[y][x] = curr
                curr += 1
            for y in range(ring+1, n-ring):  # right column
                res[y][x] = curr
                curr += 1
            for x in range(n-2-ring, ring-1, -1):  # bottom row
                res[y][x] = curr
                curr += 1
            for y in range(n-2-ring, ring, -1):  # left collumn
                res[y][x] = curr
                curr += 1
        return res


class genSolution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def genN(n):
            for i in range(1, n**2 + 1):
                yield i
        curr = genN(n)
        res = [[0]*n for _ in range(n)]
        for ring in range((n//2)+1):  # amount of "rings" the matrix has
            y = ring
            for x in range(ring, n-ring):  # top row
                res[y][x] = next(curr)
            for y in range(ring+1, n-ring):  # right column
                res[y][x] = next(curr)
            for x in range(n-2-ring, ring-1, -1):  # bottom row
                res[y][x] = next(curr)
            for y in range(n-2-ring, ring, -1):  # left collumn
                res[y][x] = next(curr)

        return res


class onelineSolution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        curr = (i for i in range(1, n**2+1))
        res = [[0]*n for _ in range(n)]
        for ring in range((n//2)+1):  # amount of "rings" the matrix has
            y = ring
            for x in range(ring, n-ring):  # top row
                res[y][x] = next(curr)
            for y in range(ring+1, n-ring):  # right column
                res[y][x] = next(curr)
            for x in range(n-2-ring, ring-1, -1):  # bottom row
                res[y][x] = next(curr)
            for y in range(n-2-ring, ring, -1):  # left collumn
                res[y][x] = next(curr)

        return res
