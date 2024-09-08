from functools import lru_cache

# see pyproject.toml
__version__ = "0.3.0"
__author__ = "Saito Tsutomu <tsutomu7@hotmail.co.jp>"


class knapsack:  # noqa: N801
    """Solving the knapsack problem.

    Maximize sum of selected weight.
    Sum of selected size is les than capacity.
    Algorithm: Dynamic Optimization

    >>> import knapsack
    >>> size = [21, 11, 15, 9, 34, 25, 41, 52]
    >>> weight = [22, 12, 16, 10, 35, 26, 42, 53]
    >>> capacity = 100
    >>> knapsack.knapsack(size, weight).solve(capacity)
    (105, [0, 1, 3, 4, 5])
    """

    def __init__(self, size: list[int], weight: list[int]):
        self.size = size
        self.weight = weight

    @lru_cache(maxsize=4096 * 4096)  # noqa: B019
    def solve(self, cap: int, i: int = 0):
        if cap < 0:
            return -sum(self.weight), []
        if i == len(self.size):
            return 0, []
        res1 = self.solve(cap, i + 1)
        res2 = self.solve(cap - self.size[i], i + 1)
        res2 = (res2[0] + self.weight[i], [i] + res2[1])
        return res1 if res1[0] >= res2[0] else res2
