class Solution:
    def RotateMatrix(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        for row in matrix:
            row.reverse()


sol = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sol.RotateMatrix(matrix)

for row in matrix:
    print(row)
