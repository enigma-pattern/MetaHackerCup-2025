# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 3 - Problem B. Streetlamp Safety
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-3/problems/B
#
# Time:  O(N^2)
# Space: O(N)
#

def streetlamp_safety():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    prefix = [0]*(N+1)
    for i in range(N):
        prefix[i+1] = prefix[i]+A[i]
    dp = [[INF]*(N+1) for _ in range(2)]
    dp[0][0] = dp[1][0] = 0
    for i in range(N):
        new_dp = [[INF]*(N+1) for _ in range(2)]
        for k in range(B[i], i+1):
            new_dp[0][k] = min(dp[0][k], dp[1][k])
        for k in range(B[i]-1, i+1):
            new_dp[1][k+1] = min(dp[0][k]+(prefix[i+1]-prefix[i-k]), dp[1][k]+A[i])
        dp = new_dp
    return min(dp[i][j] for i in range(2) for j in range(N+1))

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %d' % (case+1, streetlamp_safety()))
