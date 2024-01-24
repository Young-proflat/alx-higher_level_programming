def square_matrix(matrix=[]):
    if not matrix:
        return matrix
    sqmatrix = list(map(lambda row: list(map(lambda n: n**2, row)), matrix))
    return sqmatrix

