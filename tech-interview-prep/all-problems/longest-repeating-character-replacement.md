---
title: Longest repeating character replacement
tags: [string, 'sliding-window', 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)

Description:

- Given a string s that consists of only uppercase english letters, you can perform at most k operations on that string.
- In one operation, you can choose any character of the string and change it to any other uppercase English character.
- Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Example 1:

```text
Input: s = "ABAB", k = 2

Output: 4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
```

Example 2:

```text
Input: s = "AABABBA", k = 1

Output: 4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

Note:

- Both the string's length and k will not exceed 10^4.

Thinking:

- Can this have a sliding window based implementation?

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/string/longest-repeating-character-replacement.py ':include :type=code')
<!-- tabs:end -->
