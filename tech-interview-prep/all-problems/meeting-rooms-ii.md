---
title: Meeting rooms II
tags: [array, intervals, 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Description:

- Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` `(si < ei)`, find the minimum number of conference rooms required.
- i.e Find the maximum number of overlapped intervals

Example 1:

```text
Input: [[0, 30],[5, 10],[15, 20]],
Output: 2
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/meeting-rooms-ii.py ':include :type=code')
<!-- tabs:end -->
