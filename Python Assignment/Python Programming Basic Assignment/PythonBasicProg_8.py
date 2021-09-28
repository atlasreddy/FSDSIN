def get_matrix_dimensions(mat):
    return len(mat), len(mat[0])


def add_two_matrices_q1():

    def add_two_matrices(matA, matB):
        rowsA, columnsA = get_matrix_dimensions(matA)
        rowsB, columnsB = get_matrix_dimensions(matB)

        if not (rowsA == rowsB and columnsA == columnsB):
            return "Matrix Addition is not possible"
        result = [list(map(sum, zip(*t))) for t in zip(matA, matB)]
        print(result)
        return [[matA[i][j] + matB[i][j] for j in range(columnsA)] for i in range(rowsA)]

    print(add_two_matrices(
        [[1,2,3],[4,5,6],[7,8,9]],
        [[9,8,7],[6,5,4],[3,2,1]]
    ))

    print(add_two_matrices(
        [[1,2,3],[5,6,7]],
        [[3,2,1],[2,5,8]]
    ))


def multiply_two_matrices_q2():
    def multiply_two_matrices(matA, matB):
        rowsA, columnsA = get_matrix_dimensions(matA)
        rowsB, columnsB = get_matrix_dimensions(matB)
        if not (rowsB == columnsA):
            return "Matrices cannot be multiplied"
        result = [[0]*columnsB]*rowsA
        for i in range(rowsA):
            for j in range(columnsB):
                result[i][j] = 0
                for k in range(rowsB):
                    result[i][j] += matA[i][k] * matB[k][j]
        return result

    print(multiply_two_matrices(
        [[1, 2, 3], [5, 6, 7]],
        [[3, 2], [2, 5], [1,8]]
    ))
    # 10,36],[34,96
    #
    # print(multiply_two_matrices(
    #     [[3, 2], [2, 5], [1,8]],
    #     [[1, 2, 3], [5, 6, 7]]
    # ))
    # 13,18,23],[27,34,41], [41,50,59


def transpose_matrix_q3():
    transpose = lambda mat: list(zip(*mat))
    print(transpose([[1],[2],[3]]))


def word_sort_q4():
    def word_sort(que_str):
        words = que_str.split()
        words.sort()
        return ' '.join(words)
    print(word_sort("Hello welcome to python tutorials"))


def remove_punctuation_str_q5():
    import string
    def remove_punc_str(query_str):
        print(string.punctuation)
        new_str = ""
        for char in query_str:
            if not char in string.punctuation:
                new_str += char
        return new_str
    print(remove_punc_str("glad, to see you here. "))


if __name__ == '__main__':
    add_two_matrices_q1()
    # multiply_two_matrices_q2()  # incomplete.
    transpose_matrix_q3()
    word_sort_q4()
    remove_punctuation_str_q5()
