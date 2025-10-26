# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Practice Round - Problem E. Pay Off
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/E
#
# Time:  O(QlogQ + (N + Q) * logN)
# Space: O(N + Q)
#

from sortedcontainers import SortedList

def pay_off():
    def f(a, b):
        return a%b

    N, Q, L = list(map(int, input().split()))
    X = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]
    walls = SortedList([1, L])
    group = [[] for _ in range(N)]
    for q in queries:
        if q[0] == 1:
            walls.add(q[1])
        else:
            R, S = q[1]-1, q[2]
            idx = walls.bisect_left(X[R])
            group[R].append((walls[idx-1], walls[idx], S))
    result = 0
    robots = SortedList()
    for i in reversed(range(N)):
        for l, r, s in group[i]:
            a = X[i]-l
            b = min(f(2*s-a, 2*(r-l)), r-l)
            for q in ((l+b+1, -1), (r+1, -1)):
                idx = robots.bisect_left(q)-1
                if idx < 0:
                    continue
                robot = robots[idx]
                if robot[0]-l < 0:
                    continue
                if (2*s-a)-f(2*s-a-(robot[0]-l), 2*(r-l)) >= -a:
                    result += robot[1]+1
                break
        robots.add((X[i], i))
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, pay_off()))
