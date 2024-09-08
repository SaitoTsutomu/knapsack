from knapsack import knapsack


def test_knapsack():
    size = [21, 11, 15, 9, 34, 25, 41, 52]
    weight = [22, 12, 16, 10, 35, 26, 42, 53]
    capacity = 100
    result = knapsack(size, weight).solve(capacity)
    assert result == (105, [0, 1, 3, 4, 5])
