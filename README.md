# LeetCode Memo

### TODO

一些没理解的点暂时做一下记录，方便有时间来研究。

1. [509] Fibonacci Number - Easy
   - Official Solution: Matrix Exponentiation, complexity (time/space) O(log n) / O(log n)
   - Official Solution: Golden Ratio/Binet's Formula, complexity (time/space) O(1) / O(1)
2. [341] Flatten Nested List Iterator - Medium
   - Stack solution
   - DFS
3. [1074] Number of Submatrices That Sum to Target - Hard
   - Prefix sum
   - Sliding window
   - DP
4. [1302] Deepest Leaves Sum - Medium
   - BFS
   - Queue
5. [1192] Critical Connections in a Network - Hard
   - Tarjan's algorithm
   - Graph
6. [1642] Furthest Building You Can Reach - Medium
   - Heap
7. [745] Prefix and Suffix Search - Hard
   - Trie
8. [45] Jump Game II - Medium
   - Greedy

### TOC

| #    | Title                                                                                                                                  | Difficulty | Topics                    |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------- |
| 1642 | [Furthest Building You Can Reach](./leetcode/1642.%20Furthest%20Building%20You%20Can%20Reach%20%28Medium%29.md)                        | Medium     | Binary Search, Heap       |
| 1480 | [Running Sum of 1d Array](./leetcode/1480.%20Running%20Sum%20of%201d%20Array%20%28Easy%29.md)                                          | Easy       | Array                     |
| 1423 | [Maximum Points You Can Obtain from Cards](./leetcode/1423.%20Maximum%20Points%20You%20Can%20Obtain%20from%20Cards%20%28Medium%29.md)  | Medium     | Array, DP, Sliding Window |
| 1354 | [Construct Target Array With Multiple Sums](./leetcode/1354.%20Construct%20Target%20Array%20With%20Multiple%20Sums%20%28Hard%29.md)    | Hard       | Greedy                    |
| 1302 | [Deepest Leaves Sum](./leetcode/1302.%20Deepest%20Leaves%20Sum%20%28Medium%29.md)                                                      | Medium     |                           |
| 1192 | [Critical Connections in a Network](./leetcode/1192.%20Critical%20Connections%20in%20a%20Network%20%28Hard%29.md)                      | Hard       |                           |
| 1074 | [Number of Submatrices That Sum to Target](./leetcode/1074.%20Number%20of%20Submatrices%20That%20Sum%20to%20Target%20%28Hard%29.md)    | Hard       |                           |
| 1048 | [Longest String Chain](./leetcode/1048.%20Longest%20String%20Chain%20%28Medium%29.md)                                                  | Medium     | Hash Table, DP            |
| 970  | [Powerful Integers](./leetcode/970.%20Powerful%20Integers%20%28Medium%29.md)                                                           | Medium     |                           |
| 968  | [Binary Tree Cameras](./leetcode/968.%20Binary%20Tree%20Cameras%20%28Hard%29.md)                                                       | Hard       | DP, Greedy                |
| 906  | [Super Palindromes](./leetcode/906.%20Super%20Palindromes%20%28Hard%29.md)                                                             | Hard       | Math                      |
| 816  | [Ambiguous Coordinates](./leetcode/816.%20Ambiguous%20Coordinates%20%28Medium%29.md)                                                   | Medium     | String                    |
| 745  | [Prefix and Suffix Search](./leetcode/745.%20Prefix%20and%20Suffix%20Search%20%28Hard%29.md)                                           | Hard       | Trie                      |
| 667  | [Beautiful Arrangement II](./leetcode/667.%20Beautiful%20Arrangement%20II%20%28Medium%29.md)                                           | Medium     |                           |
| 665  | [Non-decreasing Array](./leetcode/665.%20Non-decreasing%20Array%20%28Medium%29.md)                                                     | Medium     | Array                     |
| 630  | [Course Schedule III](./leetcode/630.%20Course%20Schedule%20III%20%28Hard%29.md)                                                       | Hard       | Array, DFS, Graph, BFS    |
| 609  | [Find Duplicate File in System](./leetcode/609.%20Find%20Duplicate%20File%20in%20System%20%28Medium%29.md)                             | Medium     | Hash Table, String        |
| 589  | [N-ary Tree Preorder Traversal](./leetcode/589.%20N-ary%20Tree%20Preorder%20Traversal%20%28Easy%29.md)                                 | Easy       |                           |
| 583  | [Delete Operation for Two Strings](./leetcode/583.%20Delete%20Operation%20for%20Two%20Strings%20%28Medium%29.md)                       | Medium     | String                    |
| 509  | [Fibonacci Number](./leetcode/509.%20Fibonacci%20Number%20%28Easy%29.md)                                                               | Easy       |                           |
| 341  | [Flatten Nested List Iterator](./leetcode/341.%20Flatten%20Nested%20List%20Iterator%20%28Medium%29.md)                                 | Medium     |                           |
| 304  | [Range Sum Query 2D - Immutable](./leetcode/304.%20Range%20Sum%20Query%202D%20-%20Immutable%20%28Medium%29.md)                         | Medium     | DP                        |
| 204  | [Count Primes](./leetcode/204.%20Count%20Primes%20%28Easy%29.md)                                                                       | Easy       | Math, Hash Table          |
| 120  | [Triangle](./leetcode/120.%20Triangle%20%28Medium%29.md)                                                                               | Medium     |                           |
| 114  | [Flatten Binary Tree to Linked List](./leetcode/114.%20Flatten%20Binary%20Tree%20to%20Linked%20List%20%28Medium%29.md)                 | Medium     | DFS, Tree                 |
| 109  | [Convert Sorted List to Binary Search Tree](./leetcode/109.%20Convert%20Sorted%20List%20to%20Binary%20Search%20Tree%20%28Medium%29.md) | Medium     | Linked List, DFS          |
| 86   | [Partition List](./leetcode/86.%20Partition%20List%20%28Medium%29.md)                                                                  | Medium     |                           |
| 65   | [Valid Number](./leetcode/65.%20Valid%20Number%20%28Hard%29.md)                                                                        | Hard       | Math, String              |
| 63   | [Unique Paths II](./leetcode/63.%20Unique%20Paths%20II%20%28Medium%29.md)                                                              | Medium     |                           |
| 62   | [Unique Paths](./leetcode/62.%20Unique%20Paths%20%28Medium%29.md)                                                                      | Medium     |                           |
| 48   | [Rotate Image](./leetcode/48.%20Rotate%20Image%20%28Medium%29.md)                                                                      | Medium     |                           |
| 45   | [Jump Game II](./leetcode/45.%20Jump%20Game%20II%20%28Medium%29.md)                                                                    | Medium     | Array, Greedy             |
| 39   | [Combination Sum](./leetcode/39.%20Combination%20Sum%20%28Medium%29.md)                                                                | Medium     |                           |
| 19   | [Remove Nth Node From End of List](./leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List%20%28Medium%29.md)                    | Medium     |                           |
