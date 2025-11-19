# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 2 - Problem E. Descending Platforms
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/E
#
# Time:  O(N^3)
# Space: O(N^2)
#
# pass in PyPy3 but Python3
#

def ceil_divide(a, b):
    return (a+b-1)//b

def descending_platforms():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    prefix = [0]*(N+1)
    for i in range(len(prefix)-1):
        prefix[i+1] = prefix[i]+A[i]
    best = -1
    for i in range(N):
        if best == -1 or prefix[i+1]*(best+1) > prefix[best+1]*(i+1):
            best = i
    max_cost = N**2
    dp = [-1]*(max_cost+1)
    dp[0] = 0
    prev = [-1]*(max_cost+1)
    best_i = mn = -1
    for i in range(max_cost+1):
        if dp[i] == -1:
            continue
        extra = ceil_divide(max(M-dp[i], 0), prefix[best+1])
        cost = i+extra*(best+1)
        if best_i == -1 or cost < mn:
            best_i, mn = i, cost
        for j in range(1, min(N, max_cost-i)+1):
            if not dp[i]+prefix[j] > dp[i+j]:
                continue
            dp[i+j], prev[i+j] = dp[i]+prefix[j], i
    result = [0]*N
    result[best] += ceil_divide(max(M-dp[best_i], 0), prefix[best+1])
    i = best_i
    while i:
        j = prev[i]
        result[(i-j)-1] += 1
        i = j
    for i in reversed(range(N-1)):
        result[i] += result[i+1]
    return "%s\n%s" % (sum(result), " ".join(map(str, result)))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, descending_platforms()))
