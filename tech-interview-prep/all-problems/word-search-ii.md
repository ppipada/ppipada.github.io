---
title: Word search II
tags: [trie, backtracking, 'level-5']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/word-search-ii/)

Description:

- Given a 2D board and a list of words from the dictionary, find all words in the board.
- Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
- The same letter cell may not be used more than once in a word.

Example:

```text
Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```

Note:

- All inputs are consist of lowercase letters a-z.
- The values of words are distinct.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/trie/word-search-ii.py ':include :type=code')
<!-- tabs:end -->
