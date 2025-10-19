# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 1 - Problem A2. Snake Scales (Chapter 2)
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/A2
#
# Time:  O(NlogN)
# Space: O(N)
#

class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
    def __init__(self, n):
        self.set = list(range(n))
        self.rank = [0]*n

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:  # union by rank
            x, y = y, x
        self.set[x] = self.set[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        return True

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    uf = UnionFind(N+1)
    cnt = 0
    for d, u, v in sorted([(abs(A[i+1]-A[i]), i, i+1) for i in range(N-1)]+[(A[i]-0, N, i) for i in range(N)]):
        cnt += uf.union_set(u, v)
        if cnt == N:
            break
    return d

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, solution()))
