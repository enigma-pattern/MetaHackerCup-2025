# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 1 - Problem A2. Snake Scales (Chapter 2)
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/A2
#
# Time:  O(NlogN)
# Space: O(N)
#

def binary_search(left, right, check):
    while left <= right:
        mid = left+(right - left)//2
        if check(mid):
            right = mid-1
        else:
            left = mid+1
    return left

def solution():
    def check(i):
        def bfs(u):
            result = 0
            if lookup[u]:
                return result
            lookup[u] = True
            q = [u]
            while q:
                new_q = []
                for u in q:
                    result += 1
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q = new_q
            return result

        adj = [[] for _ in range(N+1)]
        for u in range(N):
            if A[u] <= candidates[i]:
                adj[u].append(N)
                adj[N].append(u)
        for u in range(N-1):
            if abs(A[u+1]-A[u]) <= candidates[i]:
                adj[u].append(u+1)
                adj[u+1].append(u)
        lookup = [False]*(len(adj))
        return bfs(0) == len(adj)

    N = int(input())
    A = list(map(int, input().split()))
    candidates = sorted(set(abs(A[i+1]-A[i]) for i in range(N-1))|set(A))
    left, right = 0, len(candidates)-1
    return candidates[binary_search(left, right, check)]

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, solution()))
