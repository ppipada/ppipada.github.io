---
title: Valid anagram
tags: [string, 'hash-table', 'level-1']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/valid-anagram/)

Description:

- Given two strings `s` and `t`, write a function to determine if t is an anagram of s.

Example 1:

```text
Input: s = "anagram", t = "nagaram"
Output: true
```

Example 2:

```text
Input: s = "rat", t = "car"
Output: false
```

Note:

- You may assume the string contains only lowercase alphabets.

Follow up:

- What if the inputs contain unicode characters? How would you adapt your solution to such case?

Thinking:

- This can be solved either by Sorting or hashing.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/string/valid-anagram.py ':include :type=code')
<!-- tabs:end -->
