# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 3 - Problem A. Patchwork Pyramid
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-3/problems/A
#
# Time:  O(N^2)
# Space: O(N^2)
#

def patchwork_pyramid():
    N, K = list(map(int, input().split()))
    grid = [[-1]*(i+1) for i in range(N)]
    cnt = 0
    if K == 1:
        for i in range(N):
            for j in range(i+1):
                grid[i][j] = cnt
                cnt += 1
    elif K == 2:
        for i in range(N):
            for j in range(i+1):
                if j%2 == 0:
                    grid[i][j] = cnt
                    cnt += 1
                else:
                    grid[i][j] = grid[i][j-1]
    else:
        idx = 0
        for i in range(N):
            if i%2 == 0:
                for j in range(i+1):
                    grid[i][j] = idx//K
                    cnt = max(cnt, idx//K+1)
                    idx += 1
            else:
                for j in reversed(range(i+1)):
                    grid[i][j] = idx//K
                    cnt = max(cnt, idx//K+1)
                    idx += 1
                if grid[i][i] != grid[i][i-1]:
                    grid[i][i-1], grid[i-1][max(i-K+1, 0)] = grid[i-1][max(i-K+1, 0)], grid[i][i-1]
    groups = [[] for _ in range(cnt)]
    for i in range(N):
        for j in range(i+1):
            groups[grid[i][j]].append((i, j))
    result = [['.']*(i+1) for i in range(N)]
    for g in groups:
        lookup = [False]*4
        for i, j in g:
            for di, dj in DIRECTIONS:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj <= ni and result[ni][nj] != '.':
                    lookup[ord(result[ni][nj])-ord('a')] = True
        c = next(chr(ord('a')+i) for i in range(len(lookup)) if not lookup[i])
        for i, j in g:
            result[i][j] = c
    return "%s\n%s" % (cnt, "\n".join(map(lambda x: "".join(x), result)))

DIRECTIONS = ((0, 1), (-1, 0), (0, -1))
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, patchwork_pyramid()))
