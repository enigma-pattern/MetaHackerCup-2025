# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 1 - Problem D. Crash Course
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/D
#
# Time:  O(N)
# Space: O(1)
#

def crash_course():
    N = int(input())
    S = list(input().strip())
    cnt = 0
    for x in reversed(S):
        if x == 'B':
            cnt += 1
        else:
            cnt -= 1
            if cnt == -1:
                return "Alice"
    return "Bob"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, crash_course()))
