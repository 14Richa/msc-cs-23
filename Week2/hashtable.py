from random import random


def dot_product(lst_a, lst_b):
    and_list = [elt_a * elt_b for (elt_a, elt_b) in zip(lst_a, lst_b)]
    return 0 if sum(and_list) % 2 == 0 else 1

# encode a matrix as a list of lists with each row as a list.
# for instance, the example above is written as the matrix
# H = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]
# encode column vectors simply as a list of elements.
# you can use the dot_product function provided to you.


def matrix_multiplication(H, lst):
    # your code here
    result = []
    for row in H:
        result.append(dot_product(row, lst))
    return result

H = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]
lst = [1, 1, 1, 0]

result = matrix_multiplication(H, lst)
print(result)


# Generate a random m times n matrix
# see the comment next to matrix_multiplication for how your matrix must be returned.

def return_random_hash_function(m, n):
    # return a random hash function wherein each entry is chosen as 1 with probability >= 1/2 and 0 with probability < 1/2
    # your code here
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            random_num = random()
            print(random_num)
            if random_num >= 0.5:
                val = 1
            else: 
                val = 0
            row.append(val)
        matrix.append(row)
    return matrix

matrix1 = return_random_hash_function(3, 4)
# Print 
print(matrix1)