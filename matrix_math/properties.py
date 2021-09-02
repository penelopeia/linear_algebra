def transpose(m):
    # columns become rows and rows become columns
    row_size = len(m[0])
    column_size = len(m)
    m_t = []
    # make the temp matrix in appropriate size for result, np.zeros
    for r in range(row_size):
        temp = []
        for c in range(column_size):
            temp.append(0)
        m_t.append(temp)

    for i, row in enumerate(m):
        for n, e in enumerate(row):
            m_t[n][i] = e
    return m_t

def identity(m):
    col_size = len(m)
    ident = create_zeros(m)
    for i in range(col_size):
        ident[i][i] = 1
    return ident

def is_symmetric(m):
    return m

def is_orthogonal(m1, m2):
    return True

def create_zeros(m):
    # columns become rows and rows become columns
    row_size = len(m[0])
    column_size = len(m)
    m_z = []
    for r in range(row_size):
        temp = []
        for c in range(column_size):
            temp.append(0)
        m_z.append(temp)
    return m_z