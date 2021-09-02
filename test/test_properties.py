import unittest

import matrix_math.properties as prop


class TestProperties(unittest.TestCase):

    '''test the input matrix MxN now is shape NxM'''
    def test_transpose(self):
        m = [[1,2,3],[4,5,6]]
        result = prop.transpose(m)
        self.assertEqual(result, [[1, 4], [2, 5], [3, 6]])

    def test_identity(self):
        m = [[1,2,3],[4,5,6],[7,8,9]]
        result = prop.identity(m)
        self.assertEqual(result, [[1,0,0],[0,1,0],[0,0,1]])

    def test_create_zeros(self):
        result = prop.create_zeros([[1,2,3,4],[1,1,1,1]])
        self.assertEqual(result, [[0,0,0,0],[0,0,0,0]])


if __name__ == "__main__":
    unittest.main()
