---
title: Coin change
tags: ['dynamic-programming', 'level-3']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/coin-change/)

Description:

- You are given coins of different denominations and a total amount of money amount.
- Write a function to compute the fewest number of coins that you need to make up that amount.
- If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

```text
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

Example 2:

```text
Input: coins = [2], amount = 3
Output: -1
```

Note:

- You may assume that you have an infinite number of each kind of coin.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/dp/coin-change.py ':include :type=code')
<!-- tabs:end -->
