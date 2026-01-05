# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Final Round - Problem F. Reindeer Rally
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/F
#
# Time:  O(M^2 * RlogR / 64 + N * MlogM), R = remain
# Space: O(N * M + R * M^2 / 64)
#

from functools import reduce

def rotate_left(mask, l, c):
    c %= l
    low = (mask>>(l-c))
    high = (mask<<c)&((1<<l)-1)
    return high|low

# Template: https://github.com/ho94949/EGZ/blob/main/EGZ.py
# Time: O(NlogN), Space: O(N)
def Find_t(p, T, d, u, v):
    l, h = u*pow(d, -1, p) % p, p+v*pow(d, -1, p) % p
    while l+1 != h:
        m = (l+h)//2
        if T[m*d % p]:
            l = m
        else:
            h = m
    return h*d % p

def EGZ_prime(p, a):
    k = sorted(range(2*p-1), key=lambda x: a[x] % p)
    L = [False] * (2*p-1)
    for i in range(p-1):
        if a[k[1+i]] % p == a[k[p+i]] % p:
            for i in range(1+i, 1+p+i):
                L[k[i]] = True
            return L
    s = sum((a[k[i]] for i in range(p))) % p
    T, P = [False]*p, [None]*p
    T[s] = True
    for i in range(1, p):
        if T[0]:
            break
        t = Find_t(p, T, (a[k[p+i-1]]-a[k[i]]) % p, s, 0)
        T[t] = True
        P[t] = i
    c = 0
    for i in range(p):
        L[k[i]] = True
    while s != c:
        L[k[p+P[c]-1]], L[k[P[c]]] = True, False
        c = (c - (a[k[p+P[c]-1]]-a[k[P[c]]])) % p
    return L

def EGZ_composite(p, q, a):
    S, T = list(range(p-1)), [None]*(2*q-1)
    for i in range(2*q-1):
        S.extend(range((i+1)*p-1, (i+2)*p-1))
        ret = EGZ(p, [a[s] for s in S])
        T[i] = [S[j] for j in range(2*p-1) if ret[j]]
        S = [S[j] for j in range(2*p-1) if not ret[j]]
    L = [False]*(2*p*q-1)
    ret = EGZ(q, [sum(a[t] for t in T[i])//p for i in range(2*q-1)])
    for i in range(2*q-1):
        if ret[i]:
            for j in T[i]:
                L[j] = True
    return L

def EGZ(n, a):
    if n == 1:
        return [True]
    for i in range(2, n):
        if n % i == 0:
            return EGZ_composite(i, n//i, a)
    return EGZ_prime(n, a)

def reindeer_rally():
    def find_discards(remain, total):
        group = [[] for _ in range(M)]
        for i, x in enumerate(vals):  # Time: O(N * M), Space: O(M * R), R = remain
            if x != -1 and len(group[x]) < remain:
                group[x].append(i)
        groups = []
        for i in range(M):  # Time: O(MlogR), Space: O(MlogR)
            j, base = 0, 1
            while base <= len(group[i]):
                if base&len(group[i]):
                    groups.append((i, j, base))
                    j += base
                base <<= 1
        dp = [0]*(remain+1)
        dp[0] = 1
        prev = [{} for _ in range(remain+1)]
        for i, (r, _, l) in enumerate(groups):  # Time: O(MlogR * R * (M / 64) + R * M * (M / 64)) = O(M^2 * RlogR / 64), Space: O(R * M^2 / 64)
            for j in reversed(range(remain-l+1)):
                if not dp[j]:
                    continue
                new_dp = rotate_left(dp[j], M, l*r)
                mask = new_dp&~dp[j+l]
                if not mask:
                    continue
                while mask:
                    s = (mask&-mask).bit_length()-1
                    prev[j+l][s] = (i, (s-l*r)%M)
                    mask &= mask-1
                dp[j+l] |= new_dp
        s = total
        while not (dp[remain]&(1<<s)):  # Time: O(M * (M / 64)) = O(M^2 / 64), Space: O(M / 64)
            s = (s-1)%M
        result = []
        while remain:  # Time: O(R), Space: O(R)
            i, s = prev[remain][s]
            r, i, l = groups[i]
            result.extend(group[r][i:i+l])
            remain -= l
        return result

    N, M, A, B = list(map(int, input().split()))
    W = [list(map(int, input().split())) for _ in range(N)]
    vals = [x%M if x != -1 else -1 for w in W for x in w]
    cnt = reduce(lambda accu, x: accu+(1 if x != -1 else 0), vals, 0)
    total = reduce(lambda accu, x: (accu+(x if x != -1 else 0))%M, vals, 0)
    discards = find_discards(cnt%M, total)
    lookup = [v == -1 for v in vals]
    for i in discards:
        lookup[i] = True
    candidates = [[] for _ in range(M)]
    for i, v in enumerate(vals):
        if not lookup[i]:
            candidates[v].append(i+1)
    teams = []
    for _ in range(cnt//M-1):
        arr = []
        for r in range(M):
            while candidates[r] and len(arr) < 2*M-1:
                arr.append((r, candidates[r].pop()))
            if len(arr) == 2*M-1:
                break
        chosen = EGZ(M, [r for r, _ in arr])
        for idx, (r, i) in enumerate(arr):
            if not chosen[idx]:
                candidates[r].append(i)
        teams.append([i for idx, (_, i) in enumerate(arr) if chosen[idx]])
    result = A*len(teams)
    last = [i for candidate in candidates for i in candidate]
    diff = A-B*reduce(lambda accu, x: (accu+vals[x-1])%M, last, 0)
    if diff > 0:
        teams.append(last)
        result += diff
    return "%s %s\n%s" % (result, len(teams), "\n".join(" ".join(map(str, t)) for t in teams))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, reindeer_rally()))
