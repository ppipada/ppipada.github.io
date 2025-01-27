---
title: House robber II
tags: [array, 'dynamic-programming', 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/house-robber-ii/)

Description:

- You are a professional robber planning to rob houses along a street.
- Each house has a certain amount of money stashed.
- All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
- Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

```text
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
```

Example 1:

```text
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/house-robber-ii.py ':include :type=code')
<!-- tabs:end -->
