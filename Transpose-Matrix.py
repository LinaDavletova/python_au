class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        def reverse(A, x, y):
            return A[x][y]
        
        return [[reverse(A, x, y) for x in range(len(A))] for y in range(len(A[0]))]
