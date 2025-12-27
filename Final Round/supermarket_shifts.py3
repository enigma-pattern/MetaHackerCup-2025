# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Final Round - Problem A. Supermarket Shifts
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/A
#
# Time:  O(M + NlogN)
# Space: O(N)
#

class BIT(object):  # 0-indexed.
    def __init__(self, n):
        self.__bit = [0]*(n+1)  # Extra one for dummy node.

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

def supermarket_shifts():
    N, M = list(map(int, input().split()))
    A = list(map(lambda x: int(x)-1, input().split()))
    B = list(map(lambda x: int(x)-1, input().split()))
    X_Y = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    if not all((A[x] < A[y]) == (B[x] < B[y]) for x, y in X_Y):
        return -1
    lookup = [0]*N
    for i in range(N):
        lookup[B[i]] = A[i] 
    bit = BIT(N)
    result = 0
    for i in reversed(range(N)):
        result += bit.query(lookup[i]-1)
        bit.add(lookup[i], 1)
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, supermarket_shifts()))
