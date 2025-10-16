# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Practice Round - Problem A. Warm Up
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/A
#
# Time:  O(N)
# Space: O(N)
#

from collections import defaultdict

def topological_sort(adj):
    in_degree = [0]*len(adj)
    for u in range(len(adj)):
        for v in adj[u]:
            in_degree[v] += 1
    result = []
    q = [u for u in range(len(adj)) if not in_degree[u]]
    while q:
        new_q = []
        for u in q:
            result.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v]:
                    continue
                new_q.append(v)
        q = new_q
    return result

def warm_up():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    group = defaultdict(list)
    for i, x in enumerate(A):
        group[x].append(i)
    adj = [[] for _ in range(N)]
    for i, (x, y) in enumerate(zip(A, B)):
        if x == y:
            continue
        if not (x < y and group[y]):
            return -1
        adj[i].append(group[y][0])
    result = [(i+1, adj[i][0]+1) for i in topological_sort(adj) if adj[i]]
    return "%s\n%s" % (len(result), "\n".join("%d %d" % p for p in result)) if result else 0

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, warm_up()))
