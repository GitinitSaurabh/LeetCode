class Solution:
    def ZeroMatrix(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zeroRows: set[int] = set()
        zeroCols: set[int] = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j] = 0

sol = Solution()
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

sol.ZeroMatrix(matrix)

for row in matrix:
    print(row)
