---
title: Missing number
tags: [bits, array, 'level-2']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/missing-number/)

Description:

- Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

```text
Input: [3,0,1]
Output: 2
```

Example 2:

```text
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

Note:

- Your algorithm should run in linear runtime complexity.
- Could you implement it using only constant extra space complexity?

Thinking:

- We can harness the fact that XOR is its own inverse to find the missing element in linear time.
- Because we know that `nums` contains `n` numbers and that it is missing exactly one number on the range `[0..n-1][0..n−1]`, we know that nn definitely replaces the missing number in nums.
- Therefore, if we initialize an integer to nn and XOR it with every index and value, we will be left with the missing number.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/binary/missing-number.py ':include :type=code')
<!-- tabs:end -->
