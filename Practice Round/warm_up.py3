# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Practice Round - Problem A. Warm Up
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/A
#
# Time:  O(NlogN)
# Space: O(N)
#

from collections import defaultdict

def warm_up():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    group = defaultdict(list)
    for i, x in enumerate(A):
        group[x].append(i)
    result = []
    for x, y, i in sorted((x, y, i) for i, (x, y) in enumerate(zip(A, B)) if x != y):
        if not (x < y and group[y]):
            return -1
        result.append((i+1, group[y][0]+1))
    return "%s\n%s" % (len(result), "\n".join("%d %d" % p for p in result)) if result else 0

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, warm_up()))
