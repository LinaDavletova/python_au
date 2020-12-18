class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        def average(M, x, y):
            s = 0
            kol = 0
            lenx = len(M)
            leny = len(M[0])
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i >= 0 and i < lenx and j >= 0 and j < leny:
                        kol += 1
                        s += M[i][j]
            return int(s/kol)
        
        return [[average(M, x, y) for y in range(len(M[0]))] for x in range(len(M))]
