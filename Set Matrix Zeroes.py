# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row=set()
        col=set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i in row or j in col): 
                    matrix[i][j] = 0