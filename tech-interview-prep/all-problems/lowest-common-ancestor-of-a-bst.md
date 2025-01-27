---
title: Lowest common ancestor of a binary search tree
tags: [tree, 'level-2']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

Description:

- Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
- According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

```text
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

Example 2:

```text
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

Note:

- All of the nodes' values will be unique.
- p and q are different and both values will exist in the BST.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/tree/lowest-common-ancestor-of-a-bst.py ':include :type=code')
<!-- tabs:end -->
