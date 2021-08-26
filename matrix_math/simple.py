def multiplication(m1, m2):
    # columns in A must equal rows in B
    result = []
    for m in m1:
        row_result = []
        for n in m2:
            product = m*n
            row_result.append(product)
        result.append(row_result)
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
    return False

def vector_norm(v):
    return v

# matrix norm
def frobenius_norm(m):
    return m