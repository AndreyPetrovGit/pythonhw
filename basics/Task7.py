def diaginal_reverse(matrix):

    for i in range(0, len(matrix)):
        for j in range(i, len(matrix[i])):
            t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t
    return matrix

print(diaginal_reverse([[1,2,3],[4,5,6],[7,8,9],]))