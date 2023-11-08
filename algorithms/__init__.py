from .north_west import north_west
from .vogel import vogel
from .russell import russell


def check_balanced(supply, demand):
    return sum(supply) == sum(demand)


