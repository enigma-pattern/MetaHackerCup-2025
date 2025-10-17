# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Practice Round - Problem A. Warm Up
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/A
#
# Time:  O(N)
# Space: O(N)
#

def warm_up():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    group = [[] for _ in range(N+1)]
    for i, x in enumerate(A):
        group[x].append(i)
    result = []
    for g in group:
        if not g:
            continue
        for i in g:
            if A[i] == B[i]:
                continue
            if not (A[i] < B[i] and group[B[i]]):
                return -1
            result.append((i+1, group[B[i]][0]+1))
    return "%s\n%s" % (len(result), "\n".join("%d %d" % p for p in result)) if result else 0

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, warm_up()))
