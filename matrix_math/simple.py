from math import sqrt

'''
Multiply two vectors, matrices, or scalar to matrix
using the inner product for dot product required.
'''
def multiplication(m1, m2):
    # columns in m1 must equal rows in m2
    result = []
    result_row = []
    for row in m1:
        i = 0
        result_row = []
        for _ in m2[i]:
            if len(result_row):
                result.append(result_row)
            col = []
            for r in m2:
                col.append(r[i])
            d = inner_product(row, col)
            result_row.append(d)
            i += 1
    return result

# dot product
def inner_product(v1, v2):
    # given two vectors, v1(*transform)v2 = v2(*transform)v1
    result = 0
    for i, o in enumerate(v1):
        result += o*v2[i]
    return result

def outer_product(v1, v2):
    # v1v2(*transform), good for manipulating matrix representation
    result = []
    for o in v1:
        row = []
        for t in v2:
            row.append(o*t)
        result.append(row)
    return result

def vector_norm(v):
    result = 0
    for e in v:
        result += e*e
    return sqrt(result)

# matrix norm
def frobenius_norm(m):
    result = 0
    for row in m:
        for e in row:
            result += e*e
    return sqrt(result)

def add(m1, m2):
    result = m1[:]
    dim = check_equal_size(m1, m2)
    if dim == 2:
        for i, row in enumerate(result):
            for n, _ in enumerate(row):
                result[i][n] = m1[i][n] + m2[i][n]
        return result
    elif dim == 1:
        for i, _ in enumerate(result):
            result[i] = m1[i] + m2[i]
        return result
    else:
        return False

def check_equal_size(m1, m2):
    dim = 0
    try:
        if len(m1[0]) == len(m2[0]) and \
            len(m1) == len(m2):
            dim = 2
        else:
            dim = 0
    except TypeError:
        if len(m1) == len(m2):
            dim = 1
    return dim
