# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 2 - Problem C. Designing Paths
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/C
#
# Time:  O(N + RlogR), R = sum(L)
# Space: O(N + R)
#

from sortedcontainers import SortedList

def designing_paths():
    N, K, M = map(int, input().split())
    L = [list(map(int, input().split()))[1:] for _ in range(M)]
    routes = [[] for _ in range(N)]
    for i in range(len(L)):
        for j in range(len(L[i])):
            routes[L[i][j]-1].append((i, j))
    lookup = [SortedList(range(len(L[i]))) for i in range(len(L))]
    D = [-1]*N
    D[0] = 0
    q = [0]
    while q:
        new_q = []
        for u in q:
            for i, j in routes[u]:
                while True:
                    idx = lookup[i].bisect_left(j)
                    if idx == len(lookup[i]) or lookup[i][idx] > j+K:
                        break
                    v = L[i][lookup[i].pop(idx)]-1
                    if D[v] != -1:
                        continue
                    D[v] = D[u]+1
                    new_q.append(v)
        q = new_q
    return sum(D[i]*(i+1) for i in range(N))

for case in range(int(input())):
    print('Case #%d: %d' % (case + 1, designing_paths()))
