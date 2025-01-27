---
title: Same tree
tags: [tree, dfs, 'level-2']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/same-tree/)

Description:

- Given two binary trees, write a function to check if they are the same or not.
- Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

```text
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```

Example 2:

```text
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/tree/same-tree.py ':include :type=code')
<!-- tabs:end -->
