# Copyright (c) 2025 kamyu. All rights reserved.
#
# Meta Hacker Cup 2025 Practice Round - Problem C. Monkey Around
# https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/C
#
# Time:  O(N)
# Space: O(N)
#

def monkey_around():
    N = int(input())
    A = list(map(int, input().split()))
    op1, op2 = [], []
    left = 0
    while left < N:
        right = left
        while right+1 < N and A[right+1] == A[right]+1:
            right += 1
        op1.append(A[right])
        op2.append(A[left]-1)
        for _ in range(A[left]-1):
            right += 1
        left = right+1
    suffix = 0
    for i in reversed(range(len(op2)-1)):
        suffix += op2[i+1]
        op2[i] = (op2[i]-suffix)%op1[i]
    result = []
    for a, b in zip(op1, op2):
        result.append("1 %s" % a)
        for _ in range(b):
            result.append("2")
    assert(len(result) <= 2*N)
    return "%s\n%s" % (len(result), "\n".join(result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, monkey_around()))
