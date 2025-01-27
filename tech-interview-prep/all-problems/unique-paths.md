---
title: Unique paths
tags: [array, 'dynamic-programming', 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/unique-paths/)

Description:

- A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
- The robot can only move either down or right at any point in time.
- The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
- How many possible unique paths are there?

Example 1:

```text
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

Example 2:

```text
Input: m = 7, n = 3
Output: 28
```

Constraints:

- `1 <= m, n <= 100`
- It's guaranteed that the answer will be less than or equal to `2 * 10 ^ 9`.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/unique-paths.py ':include :type=code')
<!-- tabs:end -->
