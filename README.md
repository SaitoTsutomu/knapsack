`knapsack` is a package for solving knapsack problem.

* Maximize sum of selected weight.
* Sum of selected size is les than capacity.
* Algorithm: Dynamic Optimization

## Usage

```python
import knapsack
size = [21, 11, 15, 9, 34, 25, 41, 52]
weight = [22, 12, 16, 10, 35, 26, 42, 53]
capacity = 100
knapsack.knapsack(size, weight).solve(capacity)
```

See also https://pypi.org/project/ortoolpy/

## Requirements

* Python 3

## Setup

```sh
$ pip install knapsack
```

## History

* 0.0.1 (2015-6-26): first release
