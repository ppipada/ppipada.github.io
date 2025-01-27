---
title: Merge intervals
tags: [array, intervals, 'level-3']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/merge-intervals/)

Description:

- Given a collection of intervals, merge all overlapping intervals.

Example 1:

```text
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

Example 2:

```text
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/merge-intervals.py ':include :type=code')
<!-- tabs:end -->
