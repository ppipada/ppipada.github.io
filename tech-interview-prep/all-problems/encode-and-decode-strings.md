---
title: Encode and decode strings
tags: [string, 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Description:

- Design an algorithm to encode a list of strings to a string.
- The encoded string is then sent over the network and is decoded back to the original list of strings.

Note:

- The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
- Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
- Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/string/encode-and-decode-strings.py ':include :type=code')
<!-- tabs:end -->
