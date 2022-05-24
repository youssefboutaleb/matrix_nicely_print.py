import numpy as np
matrix = [[999,7,3], [1, 2,55555555]]
def matprint(M):
    x=len(str(np.array(M).max()))
    #x=the length of the big number in the matrix
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(str(M[i][j]).rjust(x), end=" ")
        print()
matprint(matrix)
