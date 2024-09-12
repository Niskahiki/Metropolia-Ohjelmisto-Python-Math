from sympy import symbols, solve

# Symbols
x, y, z = symbols("x, y, z")

# 1. a.
print("a)")
print(solve(
    [5 * x + 3 * y - 9,
     2 * x + y - 4], [x, y]))

# 1. b.
print("b)")
print(solve(
    [2 * x + y + z - 6,
     x + 3 * y + z - 2,
     2 * x + y + 2 * z - 9], [x, y, z]))

# 1. c
print("c)")
print(solve(
    [x + y + 3 * z + 1,
     3 * x + y + z - 5,
     2 * x + y + 2 * z - 2], [x, y, z]))
