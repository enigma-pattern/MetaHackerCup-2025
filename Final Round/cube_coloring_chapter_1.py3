# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Final Round - Problem C1. Cube Coloring Chapter 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/C1
#
# Time:  O(N^3)
# Space: O(N^2)
#

def cube_coloring_chapter_1():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N-1)]
    adj = [[0]*N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1):
            adj[i+1][j] = adj[j][i+1] = A[i][j]
    for i in range(N):
        adj[i][i] = 1
    M, h = max(N, 7), N//2
    result = [[[' ']*M for _ in range(M)] for _ in range(M)]
    for i in range(h):
        for j in range(N):
            result[0][2*i][j] = result[2][j][2*i] = CHARS[i]
        for j in range(h):
            if adj[i][j]:
                result[1][2*i][2*j] = CHARS[i]
    for i in range(N-h):
        for j in range(N):
            result[4][2*i][j] = result[6][j][2*i] = CHARS[i+h]
        for j in range(N-h):
            if adj[i+h][j+h]:
                result[5][2*i][2*j] = CHARS[i+h]
    for i in range(h):
        for j in range(N-h):
            if adj[i][j+h]:
                result[3][2*j][2*i] = CHARS[i]
    return "%s\n%s" % (M, "\n".join("".join(result[i][j]) for i in range(M) for j in range(M)))

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,<.>/?'\"`~\\"
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cube_coloring_chapter_1()))
