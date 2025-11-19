# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 2 - Problem D. Dividing Passcodes
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/D
#
# Time:  precompute: O(9 * MAX_K * 2^MAX_K)
#        runtime:    O(9 * min(logR, K))
# Space: O(MAX_K * 2^MAX_K)
#
# pass in PyPy3 but Python3
#

def rotate_right(mask, l, c):
    c %= l
    low = mask&((1<<c)-1)
    high = mask>>c
    return (low<<(l-c))|high

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

def dividing_passcodes():
    def get_dp(k):
        if DP[k] is None:
            dp = [[0]*(1<<(k-1)) for _ in range(k)]
            dp[0] = [1]*(1<<(k-1))
            for i in range(1, k):
                for mask in range(1<<(k-1)):
                    for d in range(1, 10):
                        new_mask = rotate_right(mask|(1<<(k-1)), k, d)
                        if new_mask&(1<<(k-1)) == 0:
                            dp[i][mask] = (dp[i][mask]+dp[i-1][new_mask])%MOD
            DP[k] = dp
        return DP[k]

    def count(s):
        result = int(s)
        dp = get_dp(k)
        for i in range(1, min(len(s), k)):
            result = (result-dp[i][0])%MOD
        mask = 0
        for i in range(min(len(s), k)):
            d = ord(s[i])-ord('0')
            for nd in range(1, d):
                new_mask = rotate_right(mask|(1<<(k-1)), k, nd)
                if new_mask&(1<<(k-1)):
                    continue
                if (len(s)-1)-i < k:
                    result = (result-dp[(len(s)-1)-i][new_mask])%MOD
            mask = rotate_right(mask|(1<<(k-1)), k, d)
            if mask&(1<<(k-1)):
                break
        return result

    L, R, K = list(input().split())
    k = int(K)
    return (count(increase(R))-count(L))%MOD

MOD = 998244353
MAX_K = 25
DP = [None]*(MAX_K+1)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, dividing_passcodes()))
