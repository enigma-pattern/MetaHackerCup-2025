# [MetaHackerCup-2025](https://www.facebook.com/codingcompetitions/hacker-cup) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-25%20%2F%2028-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.metahackercup.2025)

* Python3 solutions of Meta Hacker Cup 2025. Solution begins with `*` means it will get TLE in the largest data set.
* Total computation amount > `10^8`, which is not friendly for Python3 to solve in 5 ~ 15 seconds. A `6-minute` timer is set for uploading the result this year.
* A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.

## Rounds

* [Hacker Cup 2024](https://github.com/kamyu104/MetaHackerCup-2024)
* [Practice Round](https://github.com/kamyu104/MetaHackerCup-2025#practice-round)
* [Round 1](https://github.com/kamyu104/MetaHackerCup-2025#round-1)
* [Round 2](https://github.com/kamyu104/MetaHackerCup-2025#round-2)
* [Round 3](https://github.com/kamyu104/MetaHackerCup-2025#round-3)
* [Final Round](https://github.com/kamyu104/MetaHackerCup-2025#final-round)

## Practice Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Warm Up](https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/A)| [Python3](./Practice%20Round/warm_up.py3) [Python3](./Practice%20Round/warm_up2.py3) [Python3](./Practice%20Round/warm_up3.py3) | _O(N)_ | _O(N)_ | Easy | | Hash Table, Sort, Topological Sort |
|B| [Zone In](https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/B)| [Python3](./Practice%20Round/zone_in.py3) | _O(R * C)_ | _O(1)_ | Easy | | BFS, Flood Fill |
|C| [Monkey Around](https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/C)| [Python3](./Practice%20Round/monkey_around.py3) | _O(N)_ | _O(N)_ | Easy | | Constructive Algorithms, Prefix Sum |
|D| [Plan Out](https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/D)| [Python3](./Practice%20Round/plan_out.py3) [Python3](./Practice%20Round/plan_out2.py3)  |  _O(N + M)_ | _O(N + M)_  | Medium |  | BFS, Flood Fill, Union Find, Euler Path  |
|E| [Pay Off](https://www.facebook.com/codingcompetitions/hacker-cup/2025/practice-round/problems/E)| [Python3](./Practice%20Round/pay_off.py3) |  _O(QlogQ + (N + Q) * logN)_ | _O(N + Q)_  | Hard |  | Sorted List, Binary Search |

## Round 1
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A1| [Snake Scales (Chapter 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/A1)| [Python3](./Round%201/snake_scales_chapter_1.py3) | _O(N)_ | _O(1)_ | Easy | | Array |
|A2| [Snake Scales (Chapter 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/A2)| [Python3](./Round%201/snake_scales_chapter_2.py3) [Python3](./Round%201/snake_scales_chapter_2-2.py3) | _O(NlogN)_ | _O(N)_ | Easy | | Sort, Binary Search, BFS, Union Find |
|B1| [Final Product (Chapter 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/B1)| [Python3](./Round%201/final_product_chapter_1.py3) | _O(N)_ | _O(1)_ | Easy | | Constructive Algorithms |
|B2| [Final Product (Chapter 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/B2)| [Python3](./Round%201/final_product_chapter_2.py3) | _O(sqrt(B))_ | _O(logB)_ | Easy | | Number Theory, Combinatorics, Stars and Bars |
|C| [Narrowing Down](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/C)| [Python3](./Round%201/narrowing_down.py3) | _O(N)_ | _O(N)_ | Easy | | Prefix Sum |
|D| [Crash Course](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-1/problems/D)| [Python3](./Round%201/crash_course.py3)  | _O(N)_  | _O(1)_  | Medium | | Game Theory |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Deciding Points](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/A)| [Python3](./Round%202/deciding_points.py3) | _O(1)_ | _O(1)_ | Easy | | Math |
|B| [Defining Prizes](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/B)| [Python3](./Round%202/defining_prizes.py3) | _O(M + NlogN)_ | _O(N)_ | Easy | | Freq Table, Sort, Binary Search |
|C| [Designing Paths](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/C)| [Python3](./Round%202/designing_paths.py3) | _O(N + SlogS)_ | _O(N + S)_ | Medium | | Sorted List, BFS |
|D| [Dividing Passcodes](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/D)| [PyPy3](./Round%202/dividing_passcodes.py3) | precompute: _O(9 * MAX_K * 2^MAX_K)_<br>runtime: _O(9 * min(logR, K))_ | _O(MAX_K * 2^MAX_K)_ | Hard | | Bitmasks, DP |
|E| [Descending Platforms](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-2/problems/E)| [PyPy3](./Round%202/descending_platforms.py3) | _O(N^3)_ | _O(N^2)_ | Hard | | Prefix Sum, Greedy, DP, Backtracing, Difference Array |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Patchwork Pyramid](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-3/problems/A)| [Python3](./Round%203/patchwork_pyramid.py3) | _O(N^2)_ | _O(N^2)_ | Medium | | Constructive Algorithms |
|B| [Streetlamp Safety](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-3/problems/B)| [Python3](./Round%203/streetlamp_safety.py3) | _O(N^2)_ | _O(N)_ | Easy | | Prefix Sum, DP |
|C| [Adversarial Attack](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-3/problems/C)| [PyPy3](./Round%203/adversarial_attack.py3) | _O(N * (L + KlogK))_ | _O(L + K)_ | Hard | | KMP, Bitset DP, Binary Lifting |
|D| [Treehouse Telegram](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-3/problems/D)| [Python3](./Round%203/treehouse_telegram.py3) | _O(N * (logN)^2)_ | _O(N)_ | Medium | | HLD, LCA, Principle of Inclusion and Exclusion |
|E| [Bitstring Botcheck](https://www.facebook.com/codingcompetitions/hacker-cup/2025/round-3/problems/E)| [Python3](./Round%203/bitstring_botcheck.py3) | _O(N^2)_ | _O(N)_ | Hard | | Precompute, BFS, Bitmasks, Constructive Algorithms, Invariants |

## Final Round
You can relive the magic of the 2025 Hacker Cup World Finals by watching the [Live Stream Recording](https://www.facebook.com/hackercup/videos/1184589873879861) of the announcement of winners.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Supermarket Shifts](https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/A)| [Python3](./Final%20Round/supermarket_shifts.py3) | _O(M + NlogN)_ | _O(N)_ | Easy | | BIT, Fenwick Tree, Inversions |
|B| [Polishing Problems](https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/B)| [Python3](./Final%20Round/polishing_problems.py3) | _O(L + T * (C + K * F * N / 64) + TlogT)_ | _O()L_ | Hard | | Math, Freq Table, Sliding Window, Bag of Words, Quick Select, LCS, Bitset DP |
|C1| [Cube Coloring (Chapter 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/C1)|  | | | | | |
|C2| [Cube Coloring (Chapter 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/C2)|  | | | | | |
|D| [Wiring Wreaths](https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/D)| [Python3](./Final%20Round/wiring_wreaths.py3) | _O(N^3 * logN)_ | _O( N)_ | Medium | | Tarjan's Algorithm, BCCs, Biconnected Components, DFS, Bitmasks, Binary Search, Greedy, Backtracking, Pruning, Prefix Sum |
|E| [Lonesome Lookout](https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/E)| [PyPy3](./Final%20Round/lonesome_lookout.py3) | _O(N + LlogL)_ | _O(N + L)_ | Medium | | Combinatorics, NTT, Garner's Algorithm, Principle of Inclusion and Exclusion |
|F| [Reindeer Rally](https://www.facebook.com/codingcompetitions/hacker-cup/2025/final-round/problems/F)|  | | | | | |
