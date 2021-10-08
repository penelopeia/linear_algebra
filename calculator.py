import argparse

import matrix_math.simple as simp

parser = argparse.ArgumentParser(description='Linear Algebra Operations.')
parser.add_argument('--a_matrix', type=[], help='first matrix to operate on')
parser.add_argument('--b_matrix', type=[], help='second matrix to operate on')

# add calculator functions as args/options
parser.add_argument('--dot', type=bool, help='set operation as dot product', nargs='?')
parser.add_argument('--add', type=bool, help='set operation as addition', nargs='?')

args = parser.parse_args()
if args.dot:
    print(simp.inner_product(args.a_matrix, args.b_matrix))
if args.add:
    print(simp.add(args.a_matrix, args.b_matrix))
else:
    print("specify operation with CLI param. See -h for details")