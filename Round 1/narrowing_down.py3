# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 1 - Problem C. Narrowing Down
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/C
#
# Time:  O(N)
# Space: O(N)
#

from collections import defaultdict

def narrowing_down():
    def f(x):
        return x*(x+1)//2

    N = int(input())
    A = list(map(int, input().split()))
    result = N*(N+1)*(N+2)//6  # sum((i+1)*(N-i) for i in range(N))
    prefix = 0
    lookup = defaultdict(int, {0: 1})
    for x in A:
        prefix ^= x
        result -= f(lookup[prefix])
        lookup[prefix] += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, narrowing_down()))
