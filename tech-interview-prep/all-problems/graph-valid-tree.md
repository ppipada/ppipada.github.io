---
title: Graph valid tree
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

- Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

```text
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
```

Hint:

- Given n = 5 and edges = `[[0, 1], [1, 2], [3, 4]]`, what should your return?
- Is this case a valid tree? According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
- Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together inedges.
- Treating input as graph, making sure no cycles and one connected component.
- Check for cycle and connectness in Graph can be done by DFS, BFS and Union-find

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/graph/graph-valid-tree.py ':include :type=code')
<!-- tabs:end -->
