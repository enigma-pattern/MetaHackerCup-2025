# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 1 - Problem B1. Final Product (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/B1
#
# Time:  O(sqrt(B) + (logB)^2 * log(logB))
# Space: O(1)
#

from collections import defaultdict
from functools import reduce

MOD = 10**9+7
def mod_inv(x):
    return pow(x, MOD-2, MOD)

def nCr(n, k):
    if n-k < k:
        k = n-k
    result = 1
    for i in range(k):
        result = (result*(n-i))*mod_inv(i+1)%MOD
    return result

def nHr(n, k):
    return nCr(n+k-1, n)

def prime_factors(x):
    cnt = defaultdict(int)
    while x%2 == 0:
        cnt[2] += 1
        x //= 2
    p = 3
    while p*p <= x:
        while x%p == 0:
            cnt[p] += 1
            x //= p
        p += 2
    if x != 1:
        cnt[x] += 1
    return cnt

def factors(n):
    for i in range(1, n+1):
        if i*i > n:
            break
        if n%i:
            continue
        yield i
        if n//i != i:
            yield n//i

def solution():
    def count(factors):
        return reduce(lambda a, b: a*b % MOD, (nHr(x, N) for x in factors.values()), 1)

    N, A, B = list(map(int, input().split()))
    B_factors = prime_factors(B)
    result = 0
    for d in factors(B):
        if d > A:
            continue
        factors1 = defaultdict(int)
        x = d
        for p in B_factors.keys():
            cnt = 0
            while not x%p:
                x //= p
                cnt += 1
            if cnt:
                factors1[p] = cnt
        factors2 = {}
        for p, x in B_factors.items():
            factors2[p] = x-factors1[p]
        result = (result+count(factors1)*count(factors2))%MOD
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, solution()))
