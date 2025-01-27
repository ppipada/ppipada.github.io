---
title: Meeting rooms
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

- Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` `(si < ei)`, determine if a person could attend all meetings.

Example 1:

```text
Input: [[0, 30],[5, 10],[15, 20]],
Output: false.
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/meeting-rooms.py ':include :type=code')
<!-- tabs:end -->
