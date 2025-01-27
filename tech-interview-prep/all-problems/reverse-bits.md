---
title: Reverse bits
tags: [bits, 'level-2']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/reverse-bits/)

Description:

- Reverse bits of a given 32 bits unsigned integer.

Example 1:

```text
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```

Follow up:

- If this function is called many times, how would you optimize it?

Thinking:

- We first intitialize result to 0. We then iterate from 0 to 31 (an integer has 32 bits).
- In each iteration:
  - We first shift result to the left by 1 bit.
  - Then, if the last digit of input n is 1, we add 1 to result.
  - To find the last digit of n, we just do: (n & 1)
    Example, if n=5 (101), n&1 = 101 & 001 = 001 = 1;
    however, if n = 2 (10), n&1 = 10 & 01 = 00 = 0).
  - Finally, we update n by shifting it to the right by 1 (n >>= 1). This is because the last digit is already taken care of, so we need to drop it by shifting n to the right by 1.
- At the end of the iteration, we return result.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/binary/reverse-bits.py ':include :type=code')
<!-- tabs:end -->
