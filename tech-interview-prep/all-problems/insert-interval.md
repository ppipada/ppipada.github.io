---
title: Insert interval
tags: [array, intervals, 'level-5']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/insert-interval/)

Description:

- Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
- You may assume that the intervals were initially sorted according to their start times.

Example 1:

```text
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

Example 2:

```text
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/insert-interval.py ':include :type=code')
<!-- tabs:end -->
