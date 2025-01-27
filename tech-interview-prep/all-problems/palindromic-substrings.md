---
title: Palindromic substrings
tags: [string, 'dynamic-programming', 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/palindromic-substrings/)

Description:

- Given a string, your task is to count how many palindromic substrings in this string.
- The substrings with different start indexes or end indexes are counted as different substrings
even they consist of same characters.

Example 1:

```text
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

Example 2:

```text
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

Note:

- The input string length won't exceed 1000.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/string/palindromic-substrings.py ':include :type=code')
<!-- tabs:end -->
