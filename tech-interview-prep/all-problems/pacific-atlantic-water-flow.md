---
title: Pacific-Atlantic water flow
tags: [graph, dfs, bfs, 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Description:

- Given an `m x n` matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
- Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
- Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Example:

```text
Input:
  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
Output:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
(positions with parentheses in above matrix).
```

Note:

- The order of returned grid coordinates does not matter.
- Both m and n are less than 150.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/graph/pacific-atlantic-water-flow.py ':include :type=code')
<!-- tabs:end -->
