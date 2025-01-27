---
title: Alien dictionary
tags: [graph, 'level-5']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Description:

- There is a new alien language which uses the latin alphabet.
- However, the order among letters are unknown to you.
- You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language.
- Derive the order of letters in this language.

Example 1:

```text
Given the following words in dictionary,
[
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]

The correct order is: "wertf".
```

Example 2:

```text
Input:
[
  "z",
  "x"
]
Output: "zx"
```

Example 3:

```text
Input:
[
  "z",
  "x",
  "z"
]
Output: ""
Explanation: The order is invalid, so return "".
```

Note:

- You may assume all letters are in lowercase.
- If the order is invalid, return an empty string.
- There may be multiple valid order of letters, return any one of them is fine.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/graph/alien-dictionary.py ':include :type=code')
<!-- tabs:end -->
