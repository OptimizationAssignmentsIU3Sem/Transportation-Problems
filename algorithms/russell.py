import numpy as np


def get_most_negative_delta(costs):
    ans = [-1, -1, float("inf")]

    col_mins = [max(costs[:, col]) for col in range(len(costs[0]))]
    for row in range(len(costs)):
        row_min = max(costs[row])
        for col in range(len(costs[row])):
            delta = costs[row][col] - (row_min + col_mins[col])
            if delta < ans[2]:
                ans = [row, col, delta]

    return tuple([ans[0], ans[1]])


def russell(costs, demand, supply):
    """
        Approximates solution to transportation model, using Russell's algorithm.
    :param costs: a matrix of costs
    :param demand: an array of demands for each destination
    :param supply: n array of number of products that sources are capable of providing
    :return: X, the set of allocations, and Z, the evaluated Z function for given allocations
    """
    demand = [[i, dem] for i, dem in enumerate(demand)]
    supply = [[i, sup] for i, sup in enumerate(supply)]
    solution = []
    z = 0

    def perform_exhaustion_check(supply_idx, demand_idx):  # need this function to be nested to reassign arrays
        nonlocal costs, supply, demand
        if supply[supply_idx][1] == 0:
            # now we have to exclude this row
            costs = np.delete(costs, supply_idx, 0)
            supply = np.delete(supply, supply_idx, 0)
        if demand[demand_idx][1] == 0:
            # now we have to exclude this column
            costs = np.delete(costs, demand_idx, 1)
            demand = np.delete(demand, demand_idx, 0)

    def perform_allocation(supply_idx, demand_idx):
        nonlocal costs, supply, demand, solution, z
        served = min(supply[supply_idx][1], demand[demand_idx][1])

        supply[supply_idx][1] -= served
        demand[demand_idx][1] -= served

        solution.append((supply[supply_idx][0], demand[demand_idx][0], served))
        z += served * costs[supply_idx][demand_idx]

    while len(costs) != 0:
        supply_idx, demand_idx = get_most_negative_delta(costs)
        perform_allocation(supply_idx, demand_idx)
        perform_exhaustion_check(supply_idx, demand_idx)

    return solution, z


def test():
    costs = np.array([[19, 30, 50, 10],
                      [70, 30, 40, 60],
                      [40, 8, 70, 20]])
    demand = np.array([5, 8, 7, 14])
    supply = np.array([7, 9, 18])

    expected_X = [(0, 0, 5), (0, 1, 2), (1, 1, 2), (1, 2, 7), (2, 1, 4), (2, 3, 14)]
    expected_Z = 807

    x, z = russell(costs, demand, supply)
    print(x)
    print(z)


if __name__ == "__main__":
    test()
