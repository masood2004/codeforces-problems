# import sys
# input = sys.stdin.readline

# t = int(input())
# for i in range(t):
#     n, k = map(int, input().split())

#     ans = k + (k - 1) // (n-1)
#     print(ans)


import sys
input = sys.stdin.readline


def count_not_divisible(X, n):
    # Total numbers minus those divisible by n
    return X - (X // n)


def solve():
    n, k = map(int, input().split())

    low = 1
    high = 2 * 10**9  # Sufficiently large upper bound
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if count_not_divisible(mid, n) >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)


t = int(input())
for _ in range(t):
    solve()
