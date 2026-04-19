import math

n, m, a, b = map(int, input().split())

only_singles = n * a
mix = (n // m) * b + (n % m) * a
only_bulk = math.ceil(n / m) * b

print(min(only_singles, mix, only_bulk))
