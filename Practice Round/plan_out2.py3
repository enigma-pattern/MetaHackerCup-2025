# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Practice Round - Problem D. Plan Out
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/D
#
# Time:  O(N + M)
# Space: O(N + M)
#

# template: https://github.com/kth-competitive-programming/kactl/blob/main/content/graph/EulerWalk.h
def euler_walk(gr, nedges, src=0):
    n = len(gr)
    D = [0]*n
    its = [0]*n
    eu = [0]*nedges
    ret = []
    s = [(src, -1)]  # modified
    D[src] += 1  # allow Euler paths, not just cycles
    while s:
        x, e = s[-1]  # modified
        it = its[x]
        end = len(gr[x])
        if it == end:
            ret.append((x, e))  # modified
            s.pop()
            continue
        y, e = gr[x][it]
        its[x] += 1
        if not eu[e]:
            D[x] -= 1
            D[y] += 1
            eu[e] = 1
            s.append((y, e))  # modified
    if any(x < 0 for x in D) or len(ret) != nedges+1:
        return []
    ret.reverse()
    return ret

def plan_out():
    def bfs(u):
        if lookup[u]:
            return False
        lookup[u] = True
        q = [u]
        while q:
            new_q = []
            for v , _ in adj[u]:
                if lookup[v]:
                    continue
                lookup[v] = True
                new_q.append(v)
            q = new_q
        return True

    N, M = list(map(int, input().split()))
    A_B = [list(map(int, input().split())) for _ in range(M)]
    edges = A_B[:]
    degree = [0]*(N+1)
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    for u in range(N+1):
        if degree[u]%2 == 0:
            continue
        edges.append((0, u))
        degree[0] += 1
        degree[u] += 1
    adj = [[] for _ in range(N+1)]
    for i, (a, b) in enumerate(edges):
        adj[a].append((b, i))
        adj[b].append((a, i))
    lookup = [False]*(N+1)
    bfs(0)
    for u in range(1, N+1):
        if not bfs(u):
            continue
        for _ in range(2):
            edges.append((0, u))
            degree[0] += 1
            degree[u] += 1
            adj[0].append((u, len(edges)-1))
            adj[u].append((0, len(edges)-1))
    assert(all(x%2 == 0 for x in degree))
    path = euler_walk(adj, len(edges), 0)
    result = [-1]*M
    for i in range(len(path)):
        if path[i][1] < M:
            result[path[i][1]] = i%2
    cnt = [[0]*(N+1) for _ in range(2)]
    for i, (a, b) in enumerate(A_B):
        cnt[result[i]][a] += 1
        cnt[result[i]][b] += 1
    total = sum(x**2 for arr in cnt for x in arr)
    return "%s %s" % (total, "".join(map(lambda x: str(x+1), result)))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, plan_out()))
