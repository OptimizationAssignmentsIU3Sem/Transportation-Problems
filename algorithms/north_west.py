import numpy as np


def north_west(costs, demand, supply):
    col, row = 0, 0
    solution_vector = []
    solution_z = 0
    while col != len(demand) or row != len(supply):
        served = min(demand[col], supply[row])
        solution_vector.append((row, col, served))
        solution_z += served * costs[row][col]
        demand[col] -= served
        supply[row] -= served
        if demand[col] == 0:
            col += 1
        if supply[row] == 0:
            row += 1

    return solution_vector, solution_z


if __name__ == "__main__":
    _costs = np.array([[2, 3, 4, 2, 4],
                       [8, 4, 1, 4, 1],
                       [9, 7, 3, 7, 2]])
    _demand = np.array([60, 70, 120, 130, 100])
    _supply = np.array([140, 180, 160])

    x, z = north_west(_costs, _demand, _supply)
    print(x)
    print(z)

