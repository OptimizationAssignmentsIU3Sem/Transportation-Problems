import numpy as np


def north_west(costs, demand, supply):
    col, row = 0, 0
    solution_vector = []
    solution_z = 0
    while col != len(demand) or row != len(supply):
        if col > len(demand) - 1 or row > len(supply) - 1:
            break
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

