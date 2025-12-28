# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Final Round - Problem E. Lonesome Lookout
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/E
#
# Time:  O(N + LlogL), L = min(R, C)
# Space: O(N + L)
#
# pass in PyPy3 but Python3
#

from functools import reduce

MOD = 10**9+7
M0, G0 = 998244353, 3
M1, G1 = 897581057, 3
M2, G2 = 880803841, 26
INV_M0_M1 = pow(M0, M1-2, M1)
INV_M0M1_M2 = pow(M0*M1, M2-2, M2)
def ntt(a, inverse, P, G):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n>>1
        while j&bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    l = 2
    if inverse:
        G = pow(G, P-2, P)
    while l <= n:
        w = pow(G, (P-1)//l, P)
        for i in range(0, n, l):
            wn = 1
            for k in range(l//2):
                u, v = a[i+k], a[i+k+l//2]*wn%P
                a[i+k], a[i+k+l//2] = (u+v)%P, (u-v)%P
                wn = wn*w%P
        l <<= 1
    if inverse:
        inv_n = pow(n, P-2, P)
        for i in range(n):
            a[i] = a[i]*inv_n%P

def ntt_conv(a, b, P, G):
    s = len(a)+len(b)-1
    n = 1<<(s-1).bit_length()
    a, b = a+[0]*(n-len(a)), b+[0]*(n-len(b))
    ntt(a, False, P, G)
    ntt(b, False, P, G)
    c = [a[i]*b[i]%P for i in range(n)]
    ntt(c, True, P, G)
    return c[:s]

def garner(r0, r1, r2):
    x0 = r0
    x1 = (r1-x0)*INV_M0_M1%M1
    x2 = (r2-x0-x1*M0)*INV_M0M1_M2%M2
    return (x0+x1*M0+x2*M0*M1)%MOD

def conv_mod(a, b):
    if not a or not b:
        return []
    c0 = ntt_conv(list(a), list(b), M0, G0)
    c1 = ntt_conv(list(a), list(b), M1, G1)
    c2 = ntt_conv(list(a), list(b), M2, G2)
    return [garner(c0[i], c1[i], c2[i]) for i in range(len(c0))]

FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
def lazy_init(n):
    while len(INV) <= n:  # lazy initialization
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)

def nCr(n, k):
    lazy_init(n)
    return (FACT[n]*INV_FACT[n-k] % MOD) * INV_FACT[k] % MOD

def factorial(n):
    lazy_init(n)
    return FACT[n]

def inv_factorial(n):
    lazy_init(n)
    return INV_FACT[n]

def lonesome_lookout():
    R, C, N = list(map(int, input().split()))
    X_Y = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
    row_cnt, col_cnt = [0]*R, [0]*C
    for X, Y in X_Y:
        row_cnt[X] += 1
        col_cnt[Y] += 1
    empty_rows = sum(c == 0 for c in row_cnt)
    empty_cols = sum(c == 0 for c in col_cnt)
    singles = sum(row_cnt[X] == 1 == col_cnt[Y] for X, Y in X_Y)
    a = []
    pow2 = 1
    for i in range(singles+1):
        a.append(nCr(singles, i)*pow2%MOD)
        pow2 = pow2*2%MOD
    b = [(nCr(empty_rows, i)*nCr(empty_cols, i)*factorial(i))%MOD for i in range(min(empty_rows, empty_cols)+1)]
    c = conv_mod(a, b)
    L = min(R, C)
    c.extend(0 for _ in range((L+1)-len(c)))
    p = pow(2, R*C-N, MOD)
    mult = pow(INV2, R+C-1, MOD)
    for i in range(L+1):
        c[i] = c[i]*p*factorial(i)%MOD
        p = p*mult%MOD
        mult = mult*4%MOD
    coef = [(1 if (L-i)%2 == 0 else -1)*inv_factorial(L-i)%MOD for i in range(L+1)]
    result = conv_mod(c, coef)
    return reduce(lambda accu, x: accu^x, ((result[L+i]*inv_factorial(i)%MOD+1220)*(i+2025) for i in range(L+1)), 0)

INV2 = pow(2, MOD-2, MOD)
for case in range(int(input())):
    print('Case #%d: %s'%(case+1, lonesome_lookout()))
