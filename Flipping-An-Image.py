class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def reverse(A, x, y):
            if A[x][len(A[x]) - y - 1]:
                return 0
            return 1
        
        return [[reverse(A, x, y) for y in range(len(A[0]))] for x in range(len(A))]
