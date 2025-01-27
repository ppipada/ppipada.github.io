---
title: Linked list cycle
tags: [linkedlist, 'level-1']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/linked-list-cycle/)

Description:

- Given a linked list, determine if it has a cycle in it.
- To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
- If pos is -1, then there is no cycle in the linked list.

Example 1:

```text
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

Example 2:

```text
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

Thinking:

- This can be solved using tortoise and hare approach or using hashtable.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/linkedlist/linked-list-cycle.py ':include :type=code')
<!-- tabs:end -->
