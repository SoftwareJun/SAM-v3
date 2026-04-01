import math
import sys 

input = lambda: sys.stdin.readline().rstrip()


def solution(n):
    flr_log_2 = n.bit_length()-1
    answer = n*flr_log_2 + n + flr_log_2-2**(flr_log_2+1) + 2
    return answer

for _ in range(int(input())):
    print(solution(int(input())))


import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t) :
    answer = 1
    i = int(input())
    nums = list(map(int, input().split()))
    k, nums = nums[0], nums[1:]
    for n in nums:
        answer *= n%10
        answer %= 10
    print(answer)

import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t) :
    length = int(input())
    nums = list(map(int, input().split()))
    print(max(nums), min(nums))


import sys

input  = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    length, nums = nums[0], nums[1:]

    current_sum = nums[0]
    max_sum = nums[0]
    start = 0
    best_start = 0
    best_end = 0
    for i in range(1, length):
        if current_sum+nums[i] <= nums[i] :
            current_sum = nums[i]
            start = i
        else:
            current_sum += nums[i]

        if (current_sum > max_sum) :
            max_sum = current_sum
            best_start = start
            best_end = i

    if max_sum <= 0:
        max_sum = 0
        best_start = -1
        best_end = -1
    
    print(max_sum, best_start, best_end)
        


import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())

length = [0]*49
length[1] = 1
length[2] = 1


for i in range(3, len(length)) :
    length[i] = length[i-1] + length[i-2]


def fibo(k, p) :
    if k == 1 :
        return 'b'
    elif k == 2 :
        return 'a'
    if p < length[k-1] :
        return fibo(k-1, p)
    else :
        return fibo(k-2, p-length[k-1])


for _ in range(t) :
    k, p = map(int, input().split())
    print(fibo(k, p))


import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

def fibo(n) :
    if n == 0 :
        return 0, 1
    f2k, f2k1 = fibo(n//2)
    a = f2k*(2*f2k1 - f2k)
    b = f2k1**2 + f2k**2
    a = a%1000
    b = b%1000

    if n % 2 == 0:
        return a, b
    else :
        return b, (a+b)%1000
        
for _ in range(t) :
    n = int(input())
    print(fibo(n)[0])
    



import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())

knight_moves = [(-2, 1),(-1, 2),(1, 2),(2,1),(2, -1),
                (1, -2),(-1,-2),(-2,-1)]

def tour(a,b, movement) :

    visited[a][b] = True
    seq[a][b] = movement

    if movement == len(seq)*len(seq[0]) :
        return 1

    for dx, dy in knight_moves :
        nx = a + dx
        ny = b + dy
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] :
            if tour(nx, ny, movement+1)==1 :
                return 1

    visited[a][b] = False
    seq[a][b] = 0
    return 0


for _ in range(t) :
    m,n,a,b = map(int, input().split())
    a -= 1
    b -= 1
    visited = []
    seq = []
    movement = 1

    for i in range(m) :
        visited.append([False]*n)
        seq.append([0]*n)
    

    num = tour(a, b, movement)

    print(num)
    if num == 1 :
        for row in seq:
            print(" ".join(map(str, row)))


import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t) :
    length = int(input())
    nums = list(map(int, input().split()))
    total_sum = 0
    for num in nums :
        total_sum += num
    
    min_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:] :
        if current_sum + num <= num :
            current_sum = current_sum + num
        else :
            current_sum = num
        if current_sum < min_sum :
            min_sum = current_sum
    
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:] :
        if current_sum + num <= num :
            current_sum = num
        else :
            current_sum += num

        if current_sum >= max_sum :
            max_sum = current_sum

    print(max(max_sum, total_sum-min_sum))


import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())



def merge_sort(arr) :
    if len(arr) <= 1:
        return arr,0
    mid = len(arr) // 2
    left, left_cnt = merge_sort(arr[:mid])
    right, right_cnt = merge_sort(arr[mid:])
    merged, cnt = merge(left, right)
    
    return merged, left_cnt+right_cnt+cnt


def merge(left, right) :
    result = []
    i=j=0
    cnt = 0

    while i<len(left) and j<len(right) :
        if left[i] > right[j] :
            result.append(right[j])
            j+=1
            cnt += len(left)-i
        else :
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result, cnt



for _ in range(t) :
    length = int(input())
    arr = list(map(int, input().split()))
    _, cnt = merge_sort(arr)
    print(cnt)
    
import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())

def relative_pos(upper, lower) :
    pos = {}
    arr = []
    for i in range(len(upper)) :
        pos[upper[i]] = i
    for i in range(len(upper)) :
        arr.append(pos[lower[i]])
    return arr

def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr, 0
    
    mid = len(arr) // 2
    left, left_cnt = merge_sort(arr[:mid])
    right, right_cnt = merge_sort(arr[mid:])
    merged, cnt = merge(left, right)
    
    return merged, left_cnt+right_cnt+cnt

def merge(left, right) :
    result = []
    cnt = 0
    i=j=0

    while i < len(left) and j < len(right) :
        if left[i] > right[j] :
            cnt += len(left) - i
            result.append(right[j])
            j += 1
        else :
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result, cnt

    

for _ in range(t) :
    length = int(input())
    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))
    arr = relative_pos(upper, lower)
    _, cnt = merge_sort(arr)
    print(cnt)



import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())

def tromino()


for _ in range(t) :
    board_size = int(input())
    x_hole, y_hole = map(int, input().split())
    board = []
    for _ in range(board_size) :
        board.append([0 for _ in range(board_size)])

    

import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())
tid = 1 

def tromino(board, size, top_x, top_y, hole_x, hole_y):
    global tid
    if size == 2: 
        for i in range(2):
            for j in range(2):
                if not (top_x+i == hole_x and top_y+j == hole_y):
                    board[top_x+i][top_y+j] = tid
        tid += 1
        return
    
    half = size // 2
    mid_x, mid_y = top_x + half, top_y + half
    
    if hole_x < mid_x and hole_y < mid_y:
        hole_quad = 1  
    elif hole_x < mid_x and hole_y >= mid_y:
        hole_quad = 2  
    elif hole_x >= mid_x and hole_y < mid_y:
        hole_quad = 3  
    else:
        hole_quad = 4 
    
    cur_id = tid
    tid += 1
    if hole_quad != 1: board[mid_x-1][mid_y-1] = cur_id
    if hole_quad != 2: board[mid_x-1][mid_y]   = cur_id
    if hole_quad != 3: board[mid_x][mid_y-1]   = cur_id
    if hole_quad != 4: board[mid_x][mid_y]     = cur_id
    
    tromino(board, half, top_x, top_y,
            hole_x if hole_quad==1 else mid_x-1,
            hole_y if hole_quad==1 else mid_y-1)
    
    tromino(board, half, top_x, mid_y,
            hole_x if hole_quad==2 else mid_x-1,
            hole_y if hole_quad==2 else mid_y)
    
    tromino(board, half, mid_x, top_y,
            hole_x if hole_quad==3 else mid_x,
            hole_y if hole_quad==3 else mid_y-1)
    
    tromino(board, half, mid_x, mid_y,
            hole_x if hole_quad==4 else mid_x,
            hole_y if hole_quad==4 else mid_y)

for _ in range(t):
    board_size = int(input())  
    x_hole, y_hole = map(int, input().split())
    
    board = [[0]*board_size for _ in range(board_size)]

    tid = 1
    tromino(board, board_size, 0, 0, x_hole, y_hole)
    
    for row in board:
        print(" ".join(map(str, row)))
    print()


import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())

def partition(arr, low, high, pivot):

    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def match_bolts_nuts(bolts, nuts, low, high, nut_index):
    if low < high:

        pivot_bolt = bolts[low]

        pivot_index = partition(nuts, low, high, pivot_bolt)

        partition(bolts, low, high, nuts[pivot_index])

        match_bolts_nuts(bolts, nuts, low, pivot_index-1, nut_index)
        match_bolts_nuts(bolts, nuts, pivot_index+1, high, nut_index)


for _ in range(t) :
    length = int(input())
    bolts = list(map(int, input().split()))
    nuts = list(map(int, input().split()))
    length = {}
    for i in range(len(bolts)) :
        length[nuts[i]] = i+1
    print(' '.join(str(length[b]) for b in bolts))


import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t) :
    target = int(input())
    coins = list(map(int, input().split()))[1:]
    dp = [0]*(target+1)
    dp[0] = 1
    for c in coins:
        for i in range(c, target+1) :
            dp[i] += dp[i-c]
    print(dp[target])


import sys

input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t) :
    n, k = map(int, input().split())
    dp = []
    for i in range(n+1) :
        dp.append([0]*(i+1))
    dp[0][0] = dp[1][0] = dp[1][1] = 1
    for i in range(2,n+1) :
        for j in range(len(dp[i])) :
            if j==0 or j==i :
                dp[i][j] = 1
            else :
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]

    print(dp[n][k])

import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(1, n + 1):

        for j in range(min(i, k), 0, -1):
            dp[j] += dp[j - 1]%10007
            dp[j] %= 10007
    print(dp[k])

import sys

input = lambda : sys.stdin.readline().rstrip()

def lcs(s1, s2) :
    memo = {}

    def solve(i, j):
        if i==len(s1) or j==len(s2):
            return 0
        if (i, j) in memo:
            return memo[(i,j)]

        if s1[i]==s2[j] :
            result = 1+solve(i+1,j+1)
        else :
            result = max(solve(i+1,j), solve(i,j+1))
            
        memo[(i,j)] = result
        return result

    return solve(0,0)

t = int(input())

for _ in range(t) :
    s1,s2 = map(str, input().split())
    print(lcs(s1,s2))


import sys
input = lambda: sys.stdin.readline().rstrip()

def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))


t = int(input())

for _ in range(t):
    s1, s2 = input().split()
    answer = lcs(s1, s2)
    print(len(answer), answer)