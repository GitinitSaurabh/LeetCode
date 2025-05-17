class Solution:
    def ZeroMatrix(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        firstRowZero = any(matrix[0][j] == 0 for j in range(cols))
        firstColZero = any(matrix[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstRowZero:
            for j in range(cols):
                matrix[0][j] = 0
        
        if firstColZero:
            for i in range(rows):
                matrix[i][0] = 0  
        

sol = Solution()
matrix = [
    [5,  1,  9, 11],
    [2,  0,  6,  8],
    [15, 7,  10, 12],
    [0, 14, 13, 16]
]

sol.ZeroMatrix(matrix)

for row in matrix:
    print(row)
