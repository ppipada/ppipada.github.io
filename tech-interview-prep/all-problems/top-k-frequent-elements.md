---
title: Top k frequent elements
tags: [heap, 'hash-table', 'level-3']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Description:

- Given a non-empty array of integers, return the k most frequent elements.

Example 1:

```text
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

Example 2:

```text
Input: nums = [1], k = 1
Output: [1]
```

Note:

- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/heap/top-k-frequent-elements.py ':include :type=code')
<!-- tabs:end -->
