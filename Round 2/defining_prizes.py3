# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 2 - Problem B. Defining Prizes
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/B
#
# Time:  O(M + NlogN)
# Space: O(N)
#

from collections import Counter

def binary_search_right(left, right, check):
    while left <= right:
        mid = left+(right-left)//2
        if not check(mid):
            right = mid-1
        else:
            left = mid+1
    return right

def defining_prizes():
    def check(c):
        total = curr = 0
        for i in range(c):
            total += sorted_cnts[i]*(c-i)
            curr += sorted_cnts[i]
            if total > prefix2[curr+1]+(prefix1[-1]-prefix1[curr+1])*curr:
                return False
        return True

    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    group = Counter(A)
    sorted_cnts = [group[x] for x in sorted(group.keys(), reverse=True)]
    cnt = [0]*(N+1)
    for x in B:
        cnt[min(x, N)] += 1
    prefix1, prefix2 = [0]*(N+2), [0]*(N+2)
    for i in range(len(cnt)):
        prefix1[i+1] = prefix1[i]+cnt[i]
        prefix2[i+1] = prefix2[i]+cnt[i]*i
    return sum(sorted_cnts[i] for i in range(binary_search_right(1, len(group), check)))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, defining_prizes()))
