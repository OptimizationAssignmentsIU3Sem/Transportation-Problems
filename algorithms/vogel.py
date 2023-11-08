import numpy as np


def get_difference(array: np.array):
    _sorted = np.sort(array)
    if len(_sorted) <= 1:
        return 0
    return _sorted[1] - _sorted[0]


def determine_max_diff(costs: np.array):
    _max = float("-inf")
    ans = []
    for dem in range(len(costs[0])):
        column = costs[:, dem]
        candidate = get_difference(column)
        if candidate > _max:
            _max = candidate
            ans = ("D", dem)

    for sup in range(len(costs)):
        row = costs[sup]
        candidate = get_difference(row)
        if candidate > _max:
            _max = candidate
            ans = ("S", sup)

    return ans


def vogel(costs, demand, supply):
    """
    Approximates solution to transportation model, using Vogel's algorithm.
    :param costs: a matrix of costs
    :param demand: an array of demands for each destination
    :param supply: n array of number of products that sources are capable of providing
    :return: Returns solution to a given transportation model. First is list of (row, col, allocation), and second is
     z-function evaluated for given answer
    """
    demand = [[i, dem] for i, dem in enumerate(demand)]
    supply = [[i, sup] for i, sup in enumerate(supply)]

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

    solution = []
    z = 0
    while len(costs) != 0:
        _type, idx = determine_max_diff(costs)
        if _type == "D":
            column = costs[:, idx]
            supply_idx = np.argmin(column)
            served = min(supply[supply_idx][1], demand[idx][1])

            supply[supply_idx][1] -= served
            demand[idx][1] -= served

            solution.append((supply[supply_idx][0], demand[idx][0], served))
            z += served * costs[supply_idx][idx]

            perform_exhaustion_check(supply_idx, idx)

        else:
            row = costs[idx]
            demand_idx = np.argmin(row)
            served = min(supply[idx][1], demand[demand_idx][1])

            supply[idx][1] -= served
            demand[demand_idx][1] -= served

            solution.append((supply[idx][0], demand[demand_idx][0], served))
            z += served * costs[idx][demand_idx]

            perform_exhaustion_check(idx, demand_idx)
    return solution, z


def test():
    _costs = np.array([[7, 8, 1, 2],
                       [4, 5, 9, 8],
                       [9, 2, 3, 6]])
    _demand = np.array([120, 50, 190, 110])
    _supply = np.array([160, 140, 170])
    sol, z = vogel(_costs, _demand, _supply)
    print(sol)
    print(z)


if __name__ == "__main__":
    test()
