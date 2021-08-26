def multiplication(m1, m2):
    # columns in A must equal rows in B
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
    return v

# matrix norm
def frobenius_norm(m):
    return m