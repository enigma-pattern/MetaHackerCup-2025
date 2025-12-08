# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Round 3 - Problem E. Bitstring Botcheck
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-3/problems/E
#
# Time:  O(N^2)
# Space: O(N)
#

def bitstring_botcheck():
    N = int(input())
    S = list(input())
    if all(S[i] <= S[i+1] for i in range(len(S)-1)):
        return "0"
    result, left, right = [], 0, 2*N-1
    while right-left+1 != 6:
        mid = left+(right-left+1)//2
        idxs = [[i for i in range(mid-2, mid+2) if S[i] == c] for c in "01"]
        excl = set(idxs[0][:2]) if len(idxs[0]) >= 2 else set(idxs[0]+idxs[1][2:])
        A = [i for i in range(left) if not i%2]+[i for i in range(left, right+1) if i < mid+2 and i not in excl]+[i for i in range(right+1, 2*N) if not i%2]
        B = [i for i in range(left) if i%2]+[i for i in range(left, right+1) if not (i < mid+2 and i not in excl)]+[i for i in range(right+1, 2*N) if i%2]
        for i in range(N):
            S[A[i]], S[B[i]] = S[B[i]], S[A[i]]
        result.append((A, B))
        if len(idxs[0]) >= 2:
            left += 2
        else:
            right -= 2
    while (mask := LOOKUP["".join(S[left:right+1])]) != -1:
        A = [i for i in range(left) if not i%2]+[left+i for i in range(right-left+1) if mask&(1<<i)]+[i for i in range(right+1, 2*N) if not i%2]
        B = [i for i in range(left) if i%2]+[left+i for i in range(right-left+1) if not mask&(1<<i)]+[i for i in range(right+1, 2*N) if i%2]
        for i in range(N):
            S[A[i]], S[B[i]] = S[B[i]], S[A[i]]
        result.append((A, B))
    return "%s\n%s" % (len(result), "\n".join(" ".join(map(lambda x: str(x+1), p)) for ps in result for p in ps))

def precompute(n):
    def popcount(x):
        return bin(x).count('1')

    lookup = {}
    q = ['0'*i+'1'*(n-i) for i in range(n+1)]
    for u in q:
        lookup[u] = -1
    while q:
        new_q = []
        for u in q:
            for mask in range(1<<n):
                if popcount(mask) != n//2:
                    continue
                A = [i for i in range(n) if mask&(1<<i)]
                B = [i for i in range(n) if not mask&(1<<i)]
                arr = list(u)
                for i in range(n//2):
                    arr[A[i]], arr[B[i]] = arr[B[i]], arr[A[i]]
                v = "".join(arr)
                if v in lookup:
                    continue
                lookup[v] = mask
                new_q.append(v)
        q = new_q
    return lookup

LOOKUP = precompute(6)
for case in range(int(input())):
    print('Case #%d: %s'%(case+1, bitstring_botcheck()))
