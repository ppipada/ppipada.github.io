---
title: Subtree of another tree
tags: [tree, 'level-3']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)

Description:

- Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
- A subtree of s is a tree consists of a node in s and all of this node's descendants.
- The tree s could also be considered as a subtree of itself.

Example 1:

```text

Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4
  / \
 1   2

 Output: true
```

Example 2:

```text
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:
   4
  / \
 1   2

Output: false
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/tree/subtree-of-another-tree.py ':include :type=code')
<!-- tabs:end -->
