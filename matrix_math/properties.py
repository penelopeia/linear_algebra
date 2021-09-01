def transpose(m):
    # columns become rows and rows become columns
    m_t = m[:]
    for i, row in enumerate(m):
        for n, e in enumerate(row):
            m_t[n][i] = e
    return m_t

def identity(m):
    return m

def is_symmetric(m):
    return m

def is_orthogonal(m1, m2):
    return True