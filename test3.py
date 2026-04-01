import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)


def pre_to_post(arr):
    i = 0
    n = len(arr)

    def dfs(upper):
        nonlocal i
        if i >= n or arr[i] > upper:
            return []
        root = arr[i]
        i += 1
        left = dfs(root)
        right = dfs(upper)
        return left + right + [root]
    return dfs(float('inf'))


def post_to_pre(arr):
    i = len(arr) - 1

    def dfs(lower):
        nonlocal i
        if i < 0 or arr[i] < lower:
            return []
        root = arr[i]
        i -= 1
        right = dfs(root)
        left = dfs(lower)
        return [root] + left + right

    return dfs(-10**18)


for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    if k == 1:
        print(*pre_to_post(nums))
    else:
        print(*post_to_pre(nums))
