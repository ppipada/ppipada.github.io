---
title: Word search
tags: [array, backtracking, 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/word-search/)

Description:

- Given a 2D board and a word, find if the word exists in the grid.
- The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
- The same letter cell may not be used more than once.

Example:

```text
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

Constraints:

- Board and word consists only of lowercase and uppercase English letters.
- 1 <= board.length <= 200
- 1 <= board[i].length <= 200
- 1 <= word.length <= 10^3

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/word-search.py ':include :type=code')
<!-- tabs:end -->
