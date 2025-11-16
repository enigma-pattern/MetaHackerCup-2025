# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 2 - Problem A. Deciding Points
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/A
#
# Time:  O(1)
# Space: O(1)
#

def deciding_points():
    N, M = list(map(int, input().split()))
    return "YES" if M <= N <= 2*M-2 or (N > 2*M-2 and N%2 == 0) else "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, deciding_points()))
