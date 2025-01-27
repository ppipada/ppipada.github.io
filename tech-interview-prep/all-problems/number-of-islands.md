---
title: Number of islands
tags: [graph, dfs, bfs, 'union-find', 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/number-of-islands/)

Description:

- Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
- An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
- You may assume all four edges of the grid are all surrounded by water.

Example 1:

```text
Input:
11110
11010
11000
00000
Output: 1
```

Example 2:

```text
Input:
11000
11000
00100
00011
Output: 3
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/graph/number-of-islands.py ':include :type=code')
<!-- tabs:end -->
