# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 3 - Problem C. Adversarial Attack
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-3/problems/C
#
# Time:  O(N * (L + KlogK / 64)), L = max length of uncompressed words
# Space: O(L + K / 64)
#
# pass in PyPy3 but Python3
#

from bitarray.util import zeros

def getPrefix(pattern):
    pattern = pattern.encode()  # modified for optimization
    prefix = [-1]*len(pattern)
    j = -1
    for i in range(1, len(pattern)):
        while j != -1 and pattern[j+1] != pattern[i]:
            j = prefix[j]
        if pattern[j+1] == pattern[i]:
            j += 1
        prefix[i] = j
    return prefix

def adversarial_attack():
    def decode(s):
        result, cnt = [], 0
        for c in s:
            if '0' <= c <= '9':
                cnt = cnt*10+(ord(c)-ord('0'))
                continue
            result.append(c*(cnt or 1))
            cnt = 0
        return "".join(result)

    def shift(dp, l):
        return zeros(l)+dp[:(K+1)-l]

    N, K = list(map(int, input().split()))
    C = [input() for _ in range(N)]
    dp, mn, prev = zeros(K+1), 0, ""
    dp[0] = 1
    for c in C:
        curr = decode(c)
        prefix = getPrefix(curr+"#"+prev)
        extras, m = [], prefix[-1]+1
        while len(curr)-m <= K-mn:
            extras.append(len(curr)-m)
            if m == 0:
                break
            m = prefix[m-1]+1
        if not extras:
            return 0
        mn += extras[0]
        new_dp, left = zeros(K+1), 0
        while left < len(extras):
            right = left
            l = extras[right+1]-extras[right] if right+1 < len(extras) else 0
            while right+1 < len(extras) and extras[right+1]-extras[right] == l:
                right += 1
            bits, cnt, base = shift(dp, extras[left]), (right-left+1)-1, 1
            while cnt:
                c = min(base, cnt)
                bits |= shift(bits, l*c)
                cnt -= c
                base <<= 1
            new_dp |= bits
            left = right+1
        dp = new_dp
        prev = curr
    return sum(i for i in range(mn, K+1) if dp[i])

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, adversarial_attack()))
