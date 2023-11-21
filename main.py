from algorithms import north_west, vogel, russell, check_balanced
import unittest
from Trans_IO import input_transport, output_transport
from algorithms import north_west, russell, vogel
import numpy as np

TEST = True
GREEN = '\033[92m'
RED = '\033[91m'


def main():
    if TEST:
        unittest.main(module="tests")

    cost_matrix, demand, supply = input_transport()
    cost_matrix, demand, supply = np.array(cost_matrix), np.array(demand), np.array(supply)
    dims = (len(cost_matrix), len(cost_matrix[0]))

    if not check_balanced(supply, demand):
        print(f"{RED}The problem is not balanced!")
        exit()

    print("Using north west to solve the problem: ")
    x, z = map(np.array, north_west(cost_matrix, demand, supply))

    output_transport(dims, x, z)

    print("Using russel to solve the problem: ")
    x_rus, z_rus = russell(cost_matrix, demand, supply)

    output_transport(dims, x_rus, z_rus)

    print("Using vogel to solve the problem: ")
    x_vog, z_vog = vogel(cost_matrix, demand, supply)

    output_transport(dims, x_vog, z_vog)


if __name__ == "__main__":
    main()
