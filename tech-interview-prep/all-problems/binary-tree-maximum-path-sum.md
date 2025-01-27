---
title: Binary tree maximum path sum
tags: [tree, dfs, 'level-5']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Description:

- Given a non-empty binary tree, find the maximum path sum.
- For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
- The path must contain at least one node and does not need to go through the root.

Example 1:

```text
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

Example 2:

```text
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/tree/binary-tree-maximum-path-sum.py ':include :type=code')
<!-- tabs:end -->
