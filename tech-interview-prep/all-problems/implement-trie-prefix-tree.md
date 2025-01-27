---
title: Implement trie (prefix tree)
tags: [trie, 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)

Description:

- Implement a trie with insert, search, and startsWith methods.
- You may assume that all inputs are consist of lowercase letters a-z.
- All inputs are guaranteed to be non-empty strings.

Example:

```text
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/trie/implement-trie-prefix-tree.py ':include :type=code')
<!-- tabs:end -->
