g = {1, 2, 3}, {2, 4, 5}, {1, 2, 3}
from functools import reduce

print(*reduce(lambda x, y: x.union(y),
              (set(input().lower()) for i in range(int(input())))))
