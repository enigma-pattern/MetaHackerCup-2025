# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 1 - Problem B1. Final Product (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/B1
#
# Time:  O(N)
# Space: O(1)
#

def solution():
    N, A, B = list(map(int, input().split()))
    result = [1]*(2*N)
    result[-1] = B
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, solution()))
