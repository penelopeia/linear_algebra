import unittest
from math import sqrt

import matrix_math.simple as simp


class TestSimple(unittest.TestCase):

    def test_inner_product(self):
        v1 = [1,2,3]
        v2 = [4,5,6]
        result = simp.inner_product(v1, v2)
        self.assertEqual(result, 32)

    def test_outer_product(self):
        v1 = [1,2,3]
        v2 = [4,5,6]
        answer = [[4,5,6],[8,10,12],[12,15,18]]
        result = simp.outer_product(v1, v2)
        self.assertEqual(result, answer)

    '''should work for scalar mult, vector, or matrix'''
    def test_multiplication(self):
        m1 = [[1,2,3],[4,5,6]]
        m2 = [[7,8],[9,10],[11,12]]
        answer = [[58,64],[139,154]]
        result = simp.multiplication(m1, m2)
        self.assertEqual(result, answer)

    def test_vector_norm(self):
        result = simp.vector_norm([1,1,1])
        self.assertEqual(result, sqrt(3))

    def test_frobenius_norm(self):
        m1 = [[1,2],[3,4]]
        result = simp.frobenius_norm(m1)
        self.assertEqual(round(result, 5), 5.47723)

    def test_add_eq_size(self):
        '''input shape must be equal and output same size'''
        m1 = [[1,2,3],[4,5,6]]
        m2 = [[1,2,3],[4,5,6]]
        answer = [[2,4,6],[8,10,12]]
        res = simp.add(m1, m2)
        self.assertEqual(res, answer)
    
    def test_add_noteq_size(self):
        '''input shape must be equal and output same size'''
        m1 = [[1,2,3],[4,5,6]]
        m2 = [[1,2,3,4],[5,6,7,8]]
        answer = False
        res = simp.add(m1, m2)
        self.assertEqual(res, answer)

    def test_equal_size(self):
        '''input shape must be equal and output same size'''
        m1 = [[1,2,3],[4,5,6]]
        m2 = [[1,2,3],[4,5,6]]
        answer = True
        res = simp.check_equal_size(m1, m2)
        self.assertEqual(res, answer)

    def test_noteq_size(self):
        '''input shape must be equal and output same size'''
        m1 = [[1,2,3],[4,5,6]]
        m2 = [[1,2,3,4],[5,6,7,8]]
        answer = False
        res = simp.check_equal_size(m1, m2)
        self.assertEqual(res, answer)


if __name__ == "__main__":
    unittest.main()
