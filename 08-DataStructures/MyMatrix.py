import random

class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        #for i in range(x):
            # create single row
        #    row = []
        #    for j in range(y):
        #        row.append(value)
            # add row to matrix
        #    matrix.append(row)
        matrix = [[0 for j in range(y)] for i in range(x)]
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
    @staticmethod
    def create_unit(x):
        m = matrix.create(x, x)
        for i in range(len(m)):
            m[i][i] = 1
        return m
    
    @staticmethod
    def fill_random(matrix, m, n):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = random.randint(m, n)
        return matrix
    
m = matrix.create(3, 5)
m = matrix.fill_random(m, 1, 9)
#m = matrix.create_unit(6)
#matrix.print(m)
#matrix.print(matrix.transpose(m))
matrix.transpose(m)
