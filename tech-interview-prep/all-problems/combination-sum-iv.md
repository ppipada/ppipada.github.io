---
title: Combination sum IV
tags: [array, 'dynamic-programming', 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/combination-sum-iv/)

Description:

- Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

```text
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
```

Follow up:

- What if negative numbers are allowed in the given array?
- How does it change the problem?
- What limitation we need to add to the question to allow negative numbers?

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/combination-sum-iv.py ':include :type=code')
<!-- tabs:end -->
