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
