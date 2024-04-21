"""
B. Покупатель рыбы
Ограничение времени 	2 секунды
Ограничение памяти 	256Mb
Ввод 	стандартный ввод или input.txt
Вывод 	стандартный вывод или output.txt
Вася решил питаться рыбой. Он решил, что в течение N дней он должен съедать по одной рыбе каждый день.
К сожалению, рыба — товар скоропортящийся и может храниться не более K дней, включая день покупки.
С помощью методов машинного обучения Вася предсказал цены на рыбу на N дней вперёд.
Помогите Васе определить, в какие дни и сколько рыбы нужно покупать, чтобы потратить как можно меньше денег.
Формат ввода
В первой строке вводится два целых числа N и K (1 ≤ N, K ≤ 100_000) — количество дней,
в течение которых нужно питаться рыбой, и срок хранения рыбы соответственно.

Во второй строке вводится N чисел, разделенных пробелами: стоимость рыбы в этот день Ci (1 ≤ Ci ≤ 106).
Формат вывода
В первой строке выведите минимальную сумму, потраченную на рыбу.
Во второй строке выведите N чисел — количество купленных рыб в каждый из дней.
Если правильных ответов несколько — выведите любой из них.
"""
from collections import deque


def fish_buyer(n: int, k: int, c: list) -> list:
    min_cost = 0
    fish_amounts = [0] * n
    min_price_indices = deque()
    for i in range(N):
        while min_price_indices and min_price_indices[0][0] < i - k + 1:
            min_price_indices.popleft()
        while min_price_indices and c[min_price_indices[-1][0]] >= c[i]:
            min_price_indices.pop()

        min_price_indices.append((i, c[i]))
        min_cost += min_price_indices[0][1]
        fish_amounts[min_price_indices[0][0]] += 1
    return fish_amounts



N, K = map(int, input().split())
C = list(map(int, input().split()))
fishes = fish_buyer(N, K, C)
sum = sum(C[i] * fishes[i] for i in range(N))
print(sum)
print(*fishes)
