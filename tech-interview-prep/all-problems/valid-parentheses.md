---
title: Valid parentheses
tags: [string, stack, 'level-1']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/valid-parentheses/)

Description:

- Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
- An input string is valid if:
  - Open brackets must be closed by the same type of brackets.
  - Open brackets must be closed in the correct order.

Example 1:

```text
Input: "()[]{}"
Output: true
```

Example 2:

```text
# Input: "([)]"
# Output: false
```

Note:

- An empty string is also considered valid.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/string/valid-parentheses.py ':include :type=code')
<!-- tabs:end -->
