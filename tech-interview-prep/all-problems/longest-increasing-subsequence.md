---
title: Longest increasing subsequence
tags: [array, 'dynamic-programming', 'binary-search', 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)

Description:

- Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

```text
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

Note:

- There may be more than one LIS combination, it is only necessary for you to return the length.
- Your algorithm should run in O(n2) complexity.

Follow up:

- Could you improve it to O(n log n) time complexity?

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/longest-increasing-subsequence.py ':include :type=code')
<!-- tabs:end -->
