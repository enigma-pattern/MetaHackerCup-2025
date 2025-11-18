# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 2 - Problem D. Dividing Passcodes
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/D
#
# Time:  precompute: O(9 * MAX_K * 2^MAX_K)
#        runtime:    O(9 * min(logR, K))
# Space: O(MAX_K * 2^MAX_K)
#

def get_dp(k):
    if DP[k] is None:
        dp = [None]*k
        dp[0] = [1]*(1<<(k-1))
        for i in range(1, k):
            dp[i] = [0]*(1<<(k-1))
            for mask in range(1<<(k-1)):
                for d in range(1, 10):
                    new_mask = add_mask(k, mask, d)
                    if new_mask != -1:
                        dp[i][mask] = (dp[i][mask]+dp[i-1][new_mask])%MOD
        DP[k] = dp
    return DP[k]

def add_mask(k, mask, d):
    def rotate_right(mask, l, c):
        c %= l
        low = mask&((1<<c)-1)
        high = mask>>c
        return (low<<(l-c))|high

    base = (d-1)%k  # shift for space optimization
    if not ((mask&(1<<base) == 0) and base != k-1):
        return -1
    return rotate_right(mask|(1<<(k-1)), k, base+1)

def dividing_passcodes():
    def increase(digits):
        result = list(digits)
        for i in reversed(range(len(result))):
            if result[i] != '9':
                result[i] = chr(ord(result[i])+1)
                break
            result[i] = '0'
        else:
            result.insert(0, '1')
        return "".join(result)

    def count(s, k):
        result = int(s)
        dp = get_dp(k)
        for i in range(1, min(len(s), k)):
            result = (result-dp[i][0])%MOD
        mask = 0
        for i in range(min(len(s), k)):
            d = ord(s[i])-ord('0')
            for nd in range(1, d):
                new_mask = add_mask(k, mask, nd)
                if new_mask == -1:
                    continue
                if (len(s)-1)-i < k:
                    result = (result-dp[(len(s)-1)-i][new_mask])%MOD
            mask = add_mask(k, mask, d)
            if mask == -1:
                break
        return result

    L, R, K = list(input().split())
    k = int(K)
    return (count(increase(R), k)-count(L, k))%MOD

MOD = 998244353
MAX_K = 25
DP = [None]*(MAX_K+1)
for case in range(int(input())):
    print('Case #%d: %d' % (case+1, dividing_passcodes()))
