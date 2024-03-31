from bisect import bisect_right


class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        s = set(arr)
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                length = 2
                while a + b in s:
                    a, b = b, a + b
                    length += 1
                ans = max(ans, length)
        return ans if ans > 2 else 0

    def lenLongestFibSubseq2(self, arr: list[int]) -> int:
        s = dict()
        f = dict(map(lambda x: (x[1], x[0]), enumerate(arr)))
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                if a + b in f:
                    s[j, f[a + b]] = s.get((i, j), 2) + 1
                    ans = max(ans, s[j, f[a + b]])
        return ans if ans > 2 else 0

    def lenLongestFibSubseq3(self, arr: list[int]) -> int:
        s = {}
        f = set()
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i - 1, -1, -1):
                a, b = arr[i], arr[j]
                c = a - b
                if c >= b:
                    break
                if c in f:
                    s[b, a] = s.get((c, b), 2) + 1
            f.add(arr[i])
        ans = max(ans, max(s.values(), default=0))
        return ans if ans > 2 else 0


def test():
    r = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]
    arr = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]
    sol = Solution()
    print(sol.lenLongestFibSubseq([1, 2, 3, 5 , 8, 13, 21, 34, 55, 89]))
    assert sol.lenLongestFibSubseq(arr) == 5
    assert sol.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]) == 3
    assert sol.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]) == 5


test()
