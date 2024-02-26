# The Millionth Fibonacci Kata
# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
# ( a b ) * ( a b ) = ( a^2+b^2 ab+bc )
# ( b c ) * ( b c ) = ( ab+bc b^2+c^2 )
# Если fib(n) = x, где n - четноё, то fib(-n) = -x
def square_matx(a, b, c):
    return a * a + b * b, a * b + b * c, a * b + b * c, b * b + c * c


def square_matx_4(a, b, c, d):
    return a * a + b * c, a * b + b * d, a * c + c * d, b * c + d * d


def multiply_matx(a, b):
    return a + b, a, b


def multiply_matx_2(a, b, c, d, e, f, g, p):
    return e * a + b * g, a * f + b * p, e * c + g * d, c * f + p * d


def fib(n):
    a, b, c, d = 1, 1, 1, 0
    e, f, g, p = 1, 1, 1, 0
    coef = 1
    if n < 0:
        n = -n
        coef = -1 if n % 2 == 0 else 1
    while n > 1:
        if n % 2:
            e, f, g, p = multiply_matx_2(a, b, c, d, e, f, g, p)
            n -= 1
        a, b, c, d = square_matx_4(a, b, c, d)
        n //= 2
    *_, d = multiply_matx_2(a, b, c, d, e, f, g, p)
    return d * coef


def exp_by_squaring(a, b, c, n):
    if n < 0:
        return exp_by_squaring(1 / x, 1, 1, -n)
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return exp_by_squaring(*square_matx(a, b, c), n / 2)
    elif n % 2:
        return x * exp_by_squaring(*square_matx(a, b, c), (n - 1) / 2)


def slow_fib(n):
    a, b = 0, 1
    if n >= 0:
        for i in range(n):
            a, b = b, a + b
    else:
        for i in range(-n):
            a, b = b - a, a
    return a


if __name__ == '__main__':
    x = 9000
    # print("123123", exp_by_squaring(1, 1, 0, 10))
    print(f'{fib(x)}')
    print(f'{fib(-x)}')
    print(f'{slow_fib(x)}')
    print(f'{slow_fib(-x)}')

"""
x^8 = 13
y^5
"""