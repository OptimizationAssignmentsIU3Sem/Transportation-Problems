from .north_west import north_west
from .vogel import vogel
from .russel import russel


def check_balanced(supply, demand):
    return sum(supply) == sum(demand)


