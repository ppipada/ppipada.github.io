---
title: Minimum window substring
tags: [string, 'hash-table', 'sliding-window', 'level-5']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/minimum-window-substring/)

Description:

- Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example 1:

```text
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

Note:

- If there is no such window in S that covers all characters in T, return the empty string "".
- If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

Thinking:

- Can this have a sliding window based approach?

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/string/minimum-window-substring.py ':include :type=code')
<!-- tabs:end -->
