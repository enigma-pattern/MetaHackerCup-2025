# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 2 - Problem B. Defining Prizes
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/B
#
# Time:  O(M + NlogN)
# Space: O(N)
#

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
        bal = curr = 0
        l = M
        for i in range(c):
            for _ in range(cnt[i]):
                curr += 1
                while l-1 >= 0 and B[l-1] < curr:
                    l -= 1
                bal += l-(c-i)
                if bal < 0:
                    return False
        return True

    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    cnt = []
    c = 0
    for i in range(len(A)):
        c += 1
        if i+1 == len(A) or A[i+1] != A[i]:
            cnt.append(c)
            c = 0
    B.sort(reverse=True)
    return sum(cnt[i] for i in range(binary_search_right(1, len(cnt), check)))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, defining_prizes()))
