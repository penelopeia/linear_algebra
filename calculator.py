import argparse

import matrix_math.simple as simp

parser = argparse.ArgumentParser(description='Linear Algebra Operations.')
parser.add_argument('--a_matrix', type=[], help='first matrix to operate on')
parser.add_argument('--b_matrix', type=[], help='second matrix to operate on')

args = parser.parse_args()
print(simp.inner_product(args.a_matrix, args.b_matrix))