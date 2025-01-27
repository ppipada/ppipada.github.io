---
title: Climbing stairs
tags: ['dynamic-programming', 'level-3']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/climbing-stairs/)

Description:

- You are climbing a stair case. It takes n steps to reach to the top.
- Each time you can either climb 1 or 2 steps.
- In how many distinct ways can you climb to the top?

Example 1:

```text
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

Example 2:

```text
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

Note:

- Given n will be a positive integer.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/dp/climbing-stairs.py ':include :type=code')
<!-- tabs:end -->
