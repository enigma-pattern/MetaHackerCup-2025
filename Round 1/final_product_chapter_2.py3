# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 1 - Problem B1. Final Product (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/B1
#
# Time:  O(sqrt(B) + (logB)^2) = O(sqrt(B))
# Space: O(logB)
#

from collections import defaultdict
from functools import reduce

MOD = 10**9+7
INV, INV_FACT = [[1]*2 for _ in range(2)]
def inv_factorial(n):
    while len(INV) <= n:  # lazy initialization
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
    return INV_FACT[n]

def nCr(n, k):
    if n-k < k:
        k = n-k
    result = inv_factorial(k)
    for i in range(k):
        result = (result*(n-i))%MOD
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
    def factors2(n):
        result = defaultdict(int)
        for p in B_factors.keys():
            cnt = 0
            while not n%p:
                n //= p
                cnt += 1
            if cnt:
                result[p] = cnt
        return result

    def count(factors):
        return reduce(lambda a, b: a*b % MOD, (nHr(x, N) for x in factors.values()), 1)

    N, A, B = list(map(int, input().split()))
    B_factors = prime_factors(B)
    result = 0
    for d in factors(B):
        if d > A:
            continue
        f1 = factors2(d)
        f2 = defaultdict(int, {p:x-f1[p] for p, x in B_factors.items()})
        result = (result+count(f1)*count(f2))%MOD
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, solution()))
