GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[34m'
RESET = '\033[0m'


def input_transport() -> tuple[list, list, list]:
    """
    Function that reads input and returns \n
    1) a costs matrix \n
    2) demand vector (1xn dimensions) \n
    3) supply vector (1xn dimensions) \n
    """

    print(BLUE + "Enter the number of rows and columns for costs matrix")

    row_num, col_num = 0, 0
    while True:
        try:
            input_args = input().split()
            if len(input_args) != 2:
                print(RED + "Only two arguments are required, please re-enter the number of variables" + BLUE)
                continue
            row_num, col_num = list(map(int, input_args))
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion for number of variables: {e}" + BLUE)

    print(f"Enter the {GREEN}{row_num}{BLUE} lines with {GREEN}{col_num}{BLUE} entries")

    cost_matrix = []
    while True:
        cost_matrix = []
        try:
            for _ in range(row_num):
                input_str = input().split()
                if len(input_str) != col_num:
                    print(RED + f'You need to enter exactly {col_num} coefficients, not {len(input_str)}' + BLUE)
                temp = list(map(int, input_str))
                cost_matrix.append(temp)
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into ints: {e}" + BLUE)

    print(f"Enter the {GREEN}{col_num}{BLUE} values of demand vector")

    demand = []
    while True:
        try:
            input_args = input().split()
            input_args_len = len(input_args)
            if input_args_len != col_num:
                print(RED + f"You need to enter exactly {col_num} values, not {input_args_len}" + BLUE)
                print("Please re-enter the values")
            var_list = list(map(int, input_args))
            demand = var_list
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into ints: {e}" + BLUE)

    print(f"Enter the {GREEN}{row_num}{BLUE} values of demand vector")

    supply = []
    while True:
        try:
            input_args = input().split()
            input_args_len = len(input_args)
            if input_args_len != row_num:
                print(RED + f"You need to enter exactly {row_num} values, not {input_args_len}" + BLUE)
                print("Please re-enter the values")
            var_list = list(map(int, input_args))
            supply = var_list
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into ints: {e}" + BLUE)

    return cost_matrix, demand, supply


def output_transport(dims: tuple[int, int], x: set, z: int) -> None:
    try:
        resulting_matrix = [[0 for _ in range(dims[1])] for _ in range(dims[0])]
        for (x, y, value) in x:
            resulting_matrix[x][y] = value

        print(f"{BLUE}The resulting choice matrix is:{GREEN}")

        for i in range(dims[0]):
            for j in range(dims[1]):
                print(resulting_matrix[i][j], end=" ")
            print()

        print(f"{BLUE}That results in {GREEN}{z}{BLUE}")
    except Exception as e:
        print(f"{RED}The method is not applicable!{BLUE}")
