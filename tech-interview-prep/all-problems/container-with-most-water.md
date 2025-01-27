---
title: Container with most water
tags: [array, 'level-2']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/container-with-most-water/)

Description:

- Given `n` non-negative integers `a1, a2, ..., an`, where each represents a point at coordinate `(i, ai)`, `n` vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
- Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Example 1:

```text
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

Note:

- You may not slant the container and n is at least 2.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/container-with-most-water.py ':include :type=code')
<!-- tabs:end -->
