# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 1 - Problem A1. Snake Scales (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/A1
#
# Time:  O(N)
# Space: O(1)
#

def snake_scales_chapter_1():
    N = int(input())
    A = list(map(int, input().split()))
    return max((abs(A[i+1]-A[i]) for i in range(N-1)), default=0)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, snake_scales_chapter_1()))
