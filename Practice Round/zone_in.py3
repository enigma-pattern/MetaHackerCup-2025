# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Practice Round - Problem B. Zone In
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/B
#
# Time:  O(R * C)
# Space: O(1)
#

def zone_in():
    def bfs():
        q = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '#']
        d = 0
        while q:
            new_q = []
            for r, c in q:
                for dr, dc in DIRECTIONS:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '.'):
                        continue
                    grid[nr][nc] = '#'
                    new_q.append((nr, nc))
            q = new_q
            d += 1
            if d == S:
                break

    def bfs2(r, c):
        result = 0
        if grid[r][c] == '#':
            return result
        grid[r][c] = '#'
        q = [(r, c)]
        while q:
            new_q = []
            for r, c in q:
                result += 1
                for dr, dc in DIRECTIONS:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '.'):
                        continue
                    grid[nr][nc] = '#'
                    new_q.append((nr, nc))
            q = new_q
        return result

    R, C, S = list(map(int, input().split()))
    grid = [['#']*(C+2)]
    for _ in range(R):
        grid.append(['#'] + list(input().strip()) + ['#'])
    grid.append(['#']*(C+2))
    bfs()
    return max(bfs2(i, j) for i in range(len(grid)) for j in range(len(grid[0])))

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, zone_in()))
