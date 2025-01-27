---
title: Validate a binary search tree
tags: [tree, dfs, 'level-2']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)

Description:

- Given a binary tree, determine if it is a valid binary search tree (BST).
- Assume a BST is defined as follows:
  - The left subtree of a node contains only nodes with keys less than the node's key.
  - The right subtree of a node contains only nodes with keys greater than the node's key.
  - Both the left and right subtrees must also be binary search trees.

Example 1:

```text
    2
   / \
  1   3

Input: [2,1,3]
Output: true
```

Example 2:

```text
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/tree/validate-binary-search-tree.py ':include :type=code')
<!-- tabs:end -->
