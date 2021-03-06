# blog-posts

## LeetCode Memo

发布方式：通过 Git 提交评论触发 GitHub Action 执行发布操作。

```shell
git commit -m "<POST_TYPE>: <COMMENT>"

# Example
git commit -m "NOTES: Publish a new note"
```

| `POST_TYPE` | 说明          |
| ----------- | ------------- |
| `NOTES`     | 笔记          |
| `STUDY`     | 研究笔记      |
| `LEETCODE`  | LeetCode 笔记 |

### TODO

一些没理解的点暂时做一下记录，方便有时间来研究。

**NOT SOLVED!!**

1. [943] FInd the Shortest Superstring - Hadr
   - TSP

**SOLVED but further research needed**

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

| Total | Easy | Medium | Hard |
| :---: | :--: | :----: | :--: |
|  84   |  18  |   49   |  17  |

| #    | Title                                                                                                                                                                                               | Difficulty | Topics                                                                       |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------- |
| 1710 | [Maximum Units on a Truck](./leetcode/1710.%20Maximum%20Units%20on%20a%20Truck%20%28Easy%29.md)                                                                                                     | Easy       | Array, Greedy, Sorting                                                       |
| 1696 | [Jump Game VI](./leetcode/1696.%20Jump%20Game%20VI%20%28Medium%29.md)                                                                                                                               | Medium     | Array, DP, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue     |
| 1695 | [Maximum Erasure Value](./leetcode/1695.%20Maximum%20Erasure%20Value%20%28Medium%29.md)                                                                                                             | Medium     | Array, Hash Table, Sliding Window                                            |
| 1689 | [Partitioning Into Minimum Number Of Deci-Binary Numbers](./leetcode/1689.%20Partitioning%20Into%20Minimum%20Number%20Of%20Deci-Binary%20Numbers%20%28Medium%29.md)                                 | Medium     | Greedy, String                                                               |
| 1642 | [Furthest Building You Can Reach](./leetcode/1642.%20Furthest%20Building%20You%20Can%20Reach%20%28Medium%29.md)                                                                                     | Medium     | Array, Greedy, Heap (Priority Queue)                                         |
| 1480 | [Running Sum of 1d Array](./leetcode/1480.%20Running%20Sum%20of%201d%20Array%20%28Easy%29.md)                                                                                                       | Easy       | Array, Prefix Sum                                                            |
| 1465 | [Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](./leetcode/1465.%20Maximum%20Area%20of%20a%20Piece%20of%20Cake%20After%20Horizontal%20and%20Vertical%20Cuts%20%28Medium%29.md) | Medium     | Array, Greedy, Sorting                                                       |
| 1423 | [Maximum Points You Can Obtain from Cards](./leetcode/1423.%20Maximum%20Points%20You%20Can%20Obtain%20from%20Cards%20%28Medium%29.md)                                                               | Medium     | Array, Sliding Window, Prefix Sum                                            |
| 1383 | [Maximum Performance of a Team](./leetcode/1383.%20Maximum%20Performance%20of%20a%20Team%20%28Hard%29.md)                                                                                           | Hard       | Array, Greedy, Sorting, Heap (Priority Queue)                                |
| 1354 | [Construct Target Array With Multiple Sums](./leetcode/1354.%20Construct%20Target%20Array%20With%20Multiple%20Sums%20%28Hard%29.md)                                                                 | Hard       | Array, Heap (Priority Queue)                                                 |
| 1302 | [Deepest Leaves Sum](./leetcode/1302.%20Deepest%20Leaves%20Sum%20%28Medium%29.md)                                                                                                                   | Medium     | Tree, DFS, BFS, Binary Tree                                                  |
| 1192 | [Critical Connections in a Network](./leetcode/1192.%20Critical%20Connections%20in%20a%20Network%20%28Hard%29.md)                                                                                   | Hard       | DFS, Graph, Biconnected Component, Need Review                               |
| 1074 | [Number of Submatrices That Sum to Target](./leetcode/1074.%20Number%20of%20Submatrices%20That%20Sum%20to%20Target%20%28Hard%29.md)                                                                 | Hard       | Array, Hash Table, Matrix, Prefix Sum                                        |
| 1048 | [Longest String Chain](./leetcode/1048.%20Longest%20String%20Chain%20%28Medium%29.md)                                                                                                               | Medium     | Array, Hash Table, Two Pointers, String, DP                                  |
| 1047 | [Remove All Adjacent Duplicates In String](./leetcode/1047.%20Remove%20All%20Adjacent%20Duplicates%20In%20String%20%28Easy%29.md)                                                                   | Easy       | String, Stack                                                                |
| 1004 | [Max Consecutive Ones III](./leetcode/1004.%20Max%20Consecutive%20Ones%20III%20%28Medium%29.md)                                                                                                     | Medium     | Array, Binary Search, Sliding Window, Prefix Sum                             |
| 970  | [Powerful Integers](./leetcode/970.%20Powerful%20Integers%20%28Medium%29.md)                                                                                                                        | Medium     | Hash Table, Math                                                             |
| 968  | [Binary Tree Cameras](./leetcode/968.%20Binary%20Tree%20Cameras%20%28Hard%29.md)                                                                                                                    | Hard       | DP, Tree, DFS, Binary Tree                                                   |
| 943  | [Find the Shortest Superstring](./leetcode/943.%20Find%20the%20Shortest%20Superstring%20%28Hard%29.md)                                                                                              | Hard       | Array, String, DP, Bit Manipulation, Bitmask, Not Solved                     |
| 906  | [Super Palindromes](./leetcode/906.%20Super%20Palindromes%20%28Hard%29.md)                                                                                                                          | Hard       | Math, Enumeration                                                            |
| 890  | [Find and Replace Pattern](./leetcode/890.%20Find%20and%20Replace%20Pattern%20%28Medium%29.md)                                                                                                      | Medium     | String, Array, Hash Table                                                    |
| 816  | [Ambiguous Coordinates](./leetcode/816.%20Ambiguous%20Coordinates%20%28Medium%29.md)                                                                                                                | Medium     | String, Backtracking                                                         |
| 792  | [Number of Matching Subsequences](./leetcode/792.%20Number%20of%20Matching%20Subsequences%20%28Medium%29.md)                                                                                        | Medium     | Hash Table, String, Trie, Sorting                                            |
| 778  | [Swim in Rising Water](./leetcode/778.%20Swim%20in%20Rising%20Water%20%28Hard%29.md)                                                                                                                | Hard       | Array, Binary Search, Heap (Priority Queue), DFS, BFS, Union Fold, Matrix    |
| 752  | [Open the Lock](./leetcode/752.%20Open%20the%20Lock%20%28Medium%29.md)                                                                                                                              | Medium     | Array, Hash Table, String, BFS                                               |
| 746  | [Min Cost Climbing Stairs](./leetcode/746.%20Min%20Cost%20Climbing%20Stairs%20%28Easy%29.md)                                                                                                        | Easy       | Array, DP                                                                    |
| 745  | [Prefix and Suffix Search](./leetcode/745.%20Prefix%20and%20Suffix%20Search%20%28Hard%29.md)                                                                                                        | Hard       | Trie                                                                         |
| 709  | [To Lower Case](./leetcode/709.%20To%20Lower%20Case%20%28Easy%29.md)                                                                                                                                | Easy       | String                                                                       |
| 695  | [Max Area of Island](./leetcode/695.%20Max%20Area%20of%20Island%20%28Medium%29.md)                                                                                                                  | Medium     | Array, DFS, BFS, Union Fold, Matrix                                          |
| 667  | [Beautiful Arrangement II](./leetcode/667.%20Beautiful%20Arrangement%20II%20%28Medium%29.md)                                                                                                        | Medium     | Array, Math                                                                  |
| 665  | [Non-decreasing Array](./leetcode/665.%20Non-decreasing%20Array%20%28Medium%29.md)                                                                                                                  | Medium     | Array                                                                        |
| 630  | [Course Schedule III](./leetcode/630.%20Course%20Schedule%20III%20%28Hard%29.md)                                                                                                                    | Hard       | Array, Greedy, Heap (Priority Queue)                                         |
| 622  | [Design Circular Queue](./leetcode/622.%20Design%20Circular%20Queue%20%28Medium%29.md)                                                                                                              | Medium     | Array, Linked List, Design, Queue                                            |
| 609  | [Find Duplicate File in System](./leetcode/609.%20Find%20Duplicate%20File%20in%20System%20%28Medium%29.md)                                                                                          | Medium     | Array, Hash Table, String                                                    |
| 589  | [N-ary Tree Preorder Traversal](./leetcode/589.%20N-ary%20Tree%20Preorder%20Traversal%20%28Easy%29.md)                                                                                              | Easy       | Stack, Tree, DFS                                                             |
| 583  | [Delete Operation for Two Strings](./leetcode/583.%20Delete%20Operation%20for%20Two%20Strings%20%28Medium%29.md)                                                                                    | Medium     | String, DP                                                                   |
| 509  | [Fibonacci Number](./leetcode/509.%20Fibonacci%20Number%20%28Easy%29.md)                                                                                                                            | Easy       | Math, DP, Recursion, Memoization                                             |
| 462  | [Minimum Moves to Equal Array Elements II](./leetcode/462.%20Minimum%20Moves%20to%20Equal%20Array%20Elements%20II%20%28Medium%29.md)                                                                | Medium     | Math, Array, Sorting                                                         |
| 453  | [Minimum Moves to Equal Array Elements](./leetcode/453.%20Minimum%20Moves%20to%20Equal%20Array%20Elements%20%28Easy%29.md)                                                                          | Easy       | Math                                                                         |
| 341  | [Flatten Nested List Iterator](./leetcode/341.%20Flatten%20Nested%20List%20Iterator%20%28Medium%29.md)                                                                                              | Medium     | Stack, Tree, DFS, Design, Queue, Iterator                                    |
| 318  | [Maximum Product of Word Lengths](./leetcode/318.%20Maximum%20Product%20of%20Word%20Lengths%20%28Medium%29.md)                                                                                      | Medium     | Bit Manipulation, Array, String                                              |
| 307  | [Range Sum Query - Mutable](./leetcode/307.%20Range%20Sum%20Query%20-%20Mutable%20%28Medium%29.md)                                                                                                  | Medium     | Array, Design, Binary Indexed Tree, Segment Tree                             |
| 304  | [Range Sum Query 2D - Immutable](./leetcode/304.%20Range%20Sum%20Query%202D%20-%20Immutable%20%28Medium%29.md)                                                                                      | Medium     | Array, Design, Matrix, Prefix Sum                                            |
| 303  | [Range Sum Query - Immutable](./leetcode/303.%20Range%20Sum%20Query%20-%20Immutable%20%28Easy%29.md)                                                                                                | Easy       | Array, Design, Prefix Sum                                                    |
| 297  | [Serialize and Deserialize Binary Tree](./leetcode/297.%20Serialize%20and%20Deserialize%20Binary%20Tree%20%28Hard%29.md)                                                                            | Hard       | String, Tree, DFS, BFS, Binary Tree, Design                                  |
| 279  | [Perfect Squares](./leetcode/279.%20Perfect%20Squares%20%28Medium%29.md)                                                                                                                            | Medium     | Math, DP, BFS                                                                |
| 236  | [Lowest Common Ancestor of a Binary Tree](./leetcode/236.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20%28Medium%29.md)                                                                  | Medium     | Tree, DFS, Binary Tree                                                       |
| 206  | [Reverse Linked List](./leetcode/206.%20Reverse%20Linked%20List%20%28Easy%29.md)                                                                                                                    | Easy       | LinkedList, Recursion                                                        |
| 204  | [Count Primes](./leetcode/204.%20Count%20Primes%20%28Easy%29.md)                                                                                                                                    | Easy       | Array, Math, Enumeration, Number Theory                                      |
| 200  | [Number of Islands](./leetcode/200.%20Number%20of%20Islands%20%28Medium%29.md)                                                                                                                      | Medium     | Array, DFS, BFS, Union Find, Matrix                                          |
| 164  | [Maximum Gap](./leetcode/164.%20Maximum%20Gap%20%28Hard%29.md)                                                                                                                                      | Hard       | Array, Sorting, Bucket Sort, Radix Sort                                      |
| 150  | [Evaluate Reverse Polish Notation](./leetcode/150.%20Evaluate%20Reverse%20Polish%20Notation%20%28Medium%29.md)                                                                                      | Medium     | Array, Math, Stack                                                           |
| 145  | [Binary Tree Postorder Traversal](./leetcode/145.%20Binary%20Tree%20Postorder%20Traversal%20%28Easy%29.md)                                                                                          | Easy       | Stack, Tree, DFS, Binary Tree                                                |
| 144  | [Binary Tree Preorder Traversal](./leetcode/144.%20Binary%20Tree%20Preorder%20Traversal%20%28Easy%29.md)                                                                                            | Easy       | Stack, Tree, DFS, Binary Tree                                                |
| 135  | [Candy](./leetcode/135.%20Candy%20%28Hard%29.md)                                                                                                                                                    | Hard       | Array, Greedy                                                                |
| 128  | [Longest Consecutive Sequence](./leetcode/128.%20Longest%20Consecutive%20Sequence%20%28Medium%29.md)                                                                                                | Medium     | Array, Hash Table, Union Find                                                |
| 120  | [Triangle](./leetcode/120.%20Triangle%20%28Medium%29.md)                                                                                                                                            | Medium     | Array, DP                                                                    |
| 118  | [Pascal's Triangle](./leetcode/118.%20Pascal%27s%20Triangle%20%28Easy%29.md)                                                                                                                        | Easy       | Array, DP                                                                    |
| 117  | [Populating Next Right Pointers in Each Node II](./leetcode/117.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II%20%28Medium%29.md)                                                  | Medium     | Tree, Binary Tree, DFS, BFS                                                  |
| 116  | [Populating Next Right Pointers in Each Node](./leetcode/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20%28Medium%29.md)                                                          | Medium     | Tree, Binary Tree, DFS, BFS                                                  |
| 114  | [Flatten Binary Tree to Linked List](./leetcode/114.%20Flatten%20Binary%20Tree%20to%20Linked%20List%20%28Medium%29.md)                                                                              | Medium     | Linked List, Stack, DFS, Tree, Binary Tree                                   |
| 112  | [Path Sum](./leetcode/112.%20Path%20Sum%20%28Easy%29.md)                                                                                                                                            | Easy       | Tree, DFS, Binary Tree                                                       |
| 109  | [Convert Sorted List to Binary Search Tree](./leetcode/109.%20Convert%20Sorted%20List%20to%20Binary%20Search%20Tree%20%28Medium%29.md)                                                              | Medium     | Linked List, Divider and Conquer, DFS, Tree, Binary Search Tree, Binary Tree |
| 106  | [Construct Binary Tree from Inorder and Postorder Traversal](./leetcode/106.%20Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal%20%28Medium%29.md)                          | Medium     | Array, Hash Table, Divide and Conquer, Tree, Binary Tree                     |
| 105  | [Construct Binary Tree from Preorder and Inorder Traversal](./leetcode/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal%20%28Medium%29.md)                            | Medium     | Array, Hash Table, Divide and Conquer, Tree, Binary Tree                     |
| 104  | [Maximum Depth of Binary Tree](./leetcode/104.%20Maximum%20Depth%20of%20Binary%20Tree%20%28Easy%29.md)                                                                                              | Easy       | Tree, BFS, DFS, Binary Tree                                                  |
| 102  | [Binary Tree Level Order Traversal](./leetcode/102.%20Binary%20Tree%20Level%20Order%20Traversal%20%28Medium%29.md)                                                                                  | Medium     | Tree, BFS, Binary Tree                                                       |
| 101  | [Symmetric Tree](./leetcode/101.%20Symmetric%20Tree%20%28Easy%29.md)                                                                                                                                | Easy       | Tree, BFS, DFS, Binary Tree                                                  |
| 97   | [Interleaving String](./leetcode/97.%20Interleaving%20String%20%28Medium%29.md)                                                                                                                     | Medium     | String, DP                                                                   |
| 94   | [Binary Tree Inorder Traversal](./leetcode/94.%20Binary%20Tree%20Inorder%20Traversal%20%28Easy%29.md)                                                                                               | Easy       | Tree, Stack, DFS, Binary Tree                                                |
| 92   | [Reverse Linked List II](./leetcode/92.%20Reverse%20Linked%20List%20II%20%28Medium%29.md)                                                                                                           | Medium     | Linked List                                                                  |
| 86   | [Partition List](./leetcode/86.%20Partition%20List%20%28Medium%29.md)                                                                                                                               | Medium     | Linked List, Two Pointers                                                    |
| 77   | [Combinations](./leetcode/77.%20Combinations%20%28Medium%29.md)                                                                                                                                     | Medium     | Array, Backtracking                                                          |
| 65   | [Valid Number](./leetcode/65.%20Valid%20Number%20%28Hard%29.md)                                                                                                                                     | Hard       | String                                                                       |
| 63   | [Unique Paths II](./leetcode/63.%20Unique%20Paths%20II%20%28Medium%29.md)                                                                                                                           | Medium     | Array, DP, Matrix                                                            |
| 62   | [Unique Paths](./leetcode/62.%20Unique%20Paths%20%28Medium%29.md)                                                                                                                                   | Medium     | Math, DP, Combinatorics                                                      |
| 52   | [N-Queens II](./leetcode/52.%20N-Queens%20II%20%28Hard%29.md)                                                                                                                                       | Hard       | Backtracking                                                                 |
| 51   | [N-Queens](./leetcode/51.%20N-Queens%20%28Hard%29.md)                                                                                                                                               | Hard       | Backtracking                                                                 |
| 48   | [Rotate Image](./leetcode/48.%20Rotate%20Image%20%28Medium%29.md)                                                                                                                                   | Medium     | Array, Math, Matrix                                                          |
| 45   | [Jump Game II](./leetcode/45.%20Jump%20Game%20II%20%28Medium%29.md)                                                                                                                                 | Medium     | Array, Greedy                                                                |
| 39   | [Combination Sum](./leetcode/39.%20Combination%20Sum%20%28Medium%29.md)                                                                                                                             | Medium     | Array, Backtracking                                                          |
| 37   | [Sudoku Solver](./leetcode/37.%20Sudoku%20Solver%20%28Hard%29.md)                                                                                                                                   | Hard       | Hash Table, Backtracking                                                     |
| 22   | [Generate Parentheses](./leetcode/22.%20Generate%20Parentheses%20%28Medium%29.md)                                                                                                                   | Medium     | String, Backtracking                                                         |
| 19   | [Remove Nth Node From End of List](./leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List%20%28Medium%29.md)                                                                                 | Medium     | Linked List, Two Pointers                                                    |
