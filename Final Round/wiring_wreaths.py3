# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Final Round - Problem D. Wiring Wreaths
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/D
#
# Time:  O(N + M + N^2 * 2^C * logN * C) = O(N^2 * logN * C * 2^C),
#        C = max number of cycles on any path (at most N/3),
#        C is typically small and greedy elimination is highly effective
# Space: O(N + M + N * C * 2^C) = O(N * C * 2^C)
#

from collections import defaultdict

def binary_search_right(left, right, check):
    while left <= right:
        mid = left+(right-left)//2
        if not check(mid):
            right = mid-1
        else:
            left = mid+1
    return right

# Template:
# Reference: https://en.wikipedia.org/wiki/Biconnected_component
def iter_tarjan_bccs(adj, cb):
    N = len(adj)
    dfn, low, idx, stack = [-1]*N, [0]*N, 0, []
    stk = [(1, (0, -1))]
    while stk:
        step, args = stk.pop()
        if step == 1:
            u, p = args
            dfn[u] = low[u] = idx
            idx += 1
            stk.append((2, (u, p, 0)))
        elif step == 2:
            u, p, i = args
            if i == len(adj[u]):
                continue
            stk.append((2, (u, p, i+1)))
            v = adj[u][i]
            if v == p:
                continue
            if dfn[v] != -1:
                low[u] = min(low[u], dfn[v])
                if dfn[v] < dfn[u]:
                    stack.append((u, v))
                continue
            stack.append((u, v))
            stk.append((3, (v, u)))
            stk.append((1, (v, u)))
        elif step == 3:
            v, u = args
            low[u] = min(low[u], low[v])
            if low[v] < dfn[u]:
                continue
            comp = []
            while stack[-1] != (u, v):
                comp.append(stack.pop())
            comp.append(stack.pop())
            cb(comp)

def wiring_wreaths():
    def build(edges):
        nodes = list({u for e in edges for u in e})
        if len(edges) == 1:
            groups.append((nodes, []))
        else:
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            cycle, visited = [nodes[0]], {nodes[0]}
            while len(cycle) < len(nodes):
                for u in adj[cycle[-1]]:
                    if u not in visited:
                        visited.add(u)
                        cycle.append(u)
                        break
            groups.append((nodes, cycle))
        for u in nodes:
            lookup[u].append(len(groups)-1)

    def iter_backtracking(remain, candidates):
        if not candidates:
            return not remain
        suffix = [0]*(len(candidates)+1)
        for i in reversed(range(len(candidates))):
            suffix[i] = suffix[i+1]|(candidates[i][0]|candidates[i][1])
        stk = [(0, remain)]
        while stk:
            i, remain = stk.pop()
            if not remain:
                return True
            if i >= len(candidates) or (remain&~suffix[i]):
                continue
            stk.append((i+1, remain&~candidates[i][1]))
            stk.append((i+1, remain&~candidates[i][0]))
        return False

    def get_mex(chosen, unchosen):
        def check(x):
            remain = ((1<<x)-1)&~chosen
            if not remain:
                return True
            candidates = []
            for mask1, mask2 in unchosen:
                new_mask1, new_mask2 = mask1&remain, mask2&remain
                if not new_mask1 and not new_mask2:
                    continue
                if (new_mask1|new_mask2) == new_mask1:
                    remain &= ~new_mask1
                elif (new_mask1|new_mask2) == new_mask2:
                    remain &= ~new_mask2
                else:
                    candidates.append((new_mask1, new_mask2))
                if not remain:
                    return True
            return iter_backtracking(remain, candidates)

        return binary_search_right(1, N, check)

    def iter_dfs():
        result = 0
        for start in range(N):
            unchosen = []
            stk = [(1, (start, -1, 1<<C[start]))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, chosen = args
                    if u > start:
                        result += get_mex(chosen, unchosen)
                    stk.append((2, (u, 0, p, chosen)))
                elif step == 2:
                    u, idx, p, chosen = args
                    if idx == len(lookup[u]):
                        continue
                    stk.append((2, (u, idx+1, p, chosen)))
                    if lookup[u][idx] == p:
                        continue
                    nodes, cycle = groups[lookup[u][idx]]
                    if not cycle:
                        v = nodes[0] if nodes[1] == u else nodes[1]
                        stk.append((1, (v, lookup[u][idx], chosen|(1<<C[v]))))
                        continue
                    stk.append((3, (cycle, 0, cycle.index(u), idx, chosen)))
                elif step == 3:
                    cycle, j, i, idx, chosen = args
                    if j == len(cycle):
                        continue
                    stk.append((3, (cycle, j+1, i, idx, chosen)))
                    if j == i:
                        continue
                    mask1 = mask2 = 0
                    for k in range(1, (j-i)%len(cycle)):
                        mask1 |= 1<<C[cycle[(i+k)%len(cycle)]]
                    for k in range(1, (i-j)%len(cycle)):
                        mask2 |= 1<<C[cycle[(j+k)%len(cycle)]]
                    unchosen.append((mask1, mask2))
                    stk.append((4, None))
                    stk.append((1, (cycle[j], lookup[cycle[i]][idx], chosen|(1<<C[cycle[j]]))))
                elif step == 4:
                    unchosen.pop()
        return result

    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A_B = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    adj = [[] for _ in range(N)]
    for u, v in A_B:
        adj[u].append(v)
        adj[v].append(u)
    groups, lookup = [], [[] for _ in range(N)]
    iter_tarjan_bccs(adj, build)
    return iter_dfs()

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, wiring_wreaths()))
