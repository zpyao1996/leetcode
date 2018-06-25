class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.accumulate=[0]
        else:
            self.accumulate=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i==0 and j==0:
                        self.accumulate[0][0]=matrix[0][0]
                    elif i==0:
                        self.accumulate[i][j]=self.accumulate[i][j-1]+matrix[i][j]
                    elif j==0:
                        self.accumulate[i][j]=self.accumulate[i-1][j]+matrix[i][j]
                    else:
                        self.accumulate[i][j]=self.accumulate[i][j-1]+self.accumulate[i-1][j] \
                                              -self.accumulate[i-1][j-1]+matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1==0 and col1==0:
            return self.accumulate[row2][col2]
        elif row1==0:
            return self.accumulate[row2][col2]-self.accumulate[row2][col1-1]
        elif col1==0:
            return self.accumulate[row2][col2]-self.accumulate[row1-1][col2]
        else:
            return self.accumulate[row2][col2]-self.accumulate[row2][col1-1]-self.accumulate[row1-1] \
            [col2]+self.accumulate[row1-1][col1-1]
matrix=[[-1]]
obj=NumMatrix(matrix)
print(obj.sumRegion(0,0,0,0))