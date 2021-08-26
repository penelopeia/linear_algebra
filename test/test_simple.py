import unittest

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

    def test_multiplication(self):
        m1 = [[1,2,3],[4,5,6]]
        m2 = [[7,8],[9,10],[11,12]]
        answer = [[58,64],[139,154]]
        result = simp.multiplication(m1, m2)
        self.assertEqual(result, answer)

if __name__ == "__main__":
    unittest.main()
