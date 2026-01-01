# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Final Round - Problem B. Polishing Problems
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/B
#
# Time:  O(L + T * (C + K * F * N / 64) + TlogT),
#        L = len(TEXT),
#        T = number of test cases,
#        C = len(cand_starts),
#        K = number of top candidates,
#        F = len(fixed_idxs) = 945
# Space: O(L)
#

from math import log
from collections import Counter
from random import randint

def nth_element(nums, n, left=0, compare=lambda a, b: a < b):
    def tri_partition(nums, left, right, target, compare):
        mid = left
        while mid <= right:
            if nums[mid] == target:
                mid += 1
            elif compare(nums[mid], target):
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        return left, right

    right = len(nums)-1
    while left <= right:
        pivot_idx = randint(left, right)
        pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
        if pivot_left <= n <= pivot_right:
            return
        elif pivot_left > n:
            right = pivot_left-1
        else:  # pivot_right < n.
            left = pivot_right+1

def log_nCr(n, k):
    return LOG_FACT[n]-LOG_FACT[k]-LOG_FACT[n-k]

def load():
    with open(TEXT_FILE) as f:
        return f.read()

def lcs_bitset(s, char_mask, mask):
    dp = 0
    for c in s:
        x = dp|char_mask.get(c, 0)
        dp = x&~(x-((dp<<1)|1))&mask
    return bin(dp).count('1')

def polishing_problems():
    _ = int(input())
    S = input()
    S_cnt = Counter(S)
    candidates = [(sum(log_nCr(cand_cnt.get(c, 0), k) for c, k in S_cnt.items()), i) for i, cand_cnt in enumerate(cand_cnts) if all(cand_cnt.get(c, 0) >= k for c, k in S_cnt.items())]
    k = min(len(candidates), K if K else float("inf"))
    nth_element(candidates, k-1, compare=lambda a, b: a[0] > b[0])
    best, best_start = (-1, -1), -1
    char_mask = {}
    for i, c in enumerate(S):
        char_mask[c] = char_mask.get(c, 0)|(1<<i)
    mask = (1<<len(S))-1
    for i in range(k):
        bag, idx = candidates[i]
        lcs = lcs_bitset("".join(TEXT[cand_starts[idx]+j] for j in fixed_idxs), char_mask, mask)
        if (lcs, bag) > best:
            best, best_start = (lcs, bag), cand_starts[idx]
    return best, best_start

L = 2025
TEXT_FILE = "ProblemText.txt"
SKIP_RATIO = 0  # 0 = answer all, 0.6 = skip 60% (answer top 40%)
K = 150  # top candidates by bag score to refine with lcs (0 = no limit)
TEXT = load()
LOG_FACT = [0.0]*(L+1)
for i in range(L):
    LOG_FACT[i+1] = LOG_FACT[i]+log(i+1)
fixed_idxs = [i for i in range(L) if i%3 == 0 or i%5 == 0]  # idx 3 and 5 could possibly be swapped but including them empirically works better since this is rare
cand_starts, cand_cnts = [], []
cnt = Counter(TEXT[i] for i in range(L))
for i in range(len(TEXT)-L+1):
    if i:
        cnt[TEXT[i-1]] -= 1
        if not cnt[TEXT[i-1]]:
            del cnt[TEXT[i-1]]
        cnt[TEXT[i+(L-1)]] += 1
    if not (TEXT[i] != ' ' and (i == 0 or TEXT[i-1] == ' ')):
        continue
    cand_starts.append(i)
    cand_cnts.append(dict(cnt))
rets = [(polishing_problems(), i) for i in range(int(input()))]
rets.sort(key=lambda x: x[0], reverse=True)
results = ["SKIP"]*len(rets)
for i in range(len(rets)-int(len(rets)*SKIP_RATIO)):
    (_, start), idx = rets[i]
    results[idx] = TEXT[start:start+L]
for case, result in enumerate(results):
    print('Case #%d: %s' % (case+1, result))
