# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Final Round - Problem C2. Cube Coloring Chapter 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/C2
#
# Time:  O(N^2 + M^3)
# Space: O(N^2)
#

def cube_coloring_chapter_2():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N-1)]
    adj = [[0]*N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1):
            adj[i+1][j] = adj[j][i+1] = A[i][j]
    for i in range(N):
        adj[i][i] = 1
    result = [[[' ']*M for _ in range(M)] for _ in range(M)]
    for idx, g in enumerate(ORDER):
        for i in range(min(G, N-g*G)):
            for z in range(2*1, 2*G+1):
                result[idx*4][2*i+2][z] = result[idx*4+2][z][2*i+2] = CHARS[g*G+i]
            for j in range(G):
                if g*G+j < N and adj[g*G+i][g*G+j]:
                    result[idx*4+1][2*j+2][2*i+2] = CHARS[g*G+i]
                if idx+1 < len(ORDER) and ORDER[idx+1]*G+j < N and adj[g*G+i][ORDER[idx+1]*G+j]:
                    result[idx*4+3][2*j+2][2*i+2] = CHARS[g*G+i]
    for g, idxs, z1, z2, rng, swap in [
        (0, [0, 6, 10], 1, 0, range(M), False),
        (1, [1, 4], 2*G+1, 2*G+2, range(1*4, 4*4+1), False),
        (4, [5, 8], 2*G+1, 2*G+2, range(5*4, 8*4+1), False),
        (2, [2, 7], 1, 0, range(M), True),
        (3, [3, 9], 2*G+1, 2*G+2, range(M), True)
    ]:
        for i in range(min(G, N-g*G)):
            for idx in idxs:
                if swap:
                    result[idx*4+2][z1][2*i+2] = result[idx*4+2][z2][2*i+2] = CHARS[g*G+i]
                else:
                    result[idx*4][2*i+2][z1] = result[idx*4][2*i+2][z2] = CHARS[g*G+i]
            for x in rng:
                if swap:
                    result[x][z2][2*i+2] = CHARS[g*G+i]
                else:
                    result[x][2*i+2][z2] = CHARS[g*G+i]
    return "%s\n%s" % (M, "\n".join("".join(result[i][j]) for i in range(M) for j in range(M)))

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,<.>/?'\"`~\\"
M, G = 43, 19
ORDER = [0, 1, 2, 3, 1, 4, 0, 2, 4, 3, 0]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cube_coloring_chapter_2()))
