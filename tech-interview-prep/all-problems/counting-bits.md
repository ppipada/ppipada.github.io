---
title: Counting bits
tags: [bits, 'dynamic-programming', array, 'level-4']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/counting-bits/)

Description:

- Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

```text
Input: 2
Output: [0,1,1]
```

Example 2:

```text
Input: 5
Output: [0,1,1,2,1,2]
```

Follow up:

- It is very easy to come up with a solution with run time O(n\*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
- Space complexity should be O(n).

Thinking:

- We do not need check the input parameter, because the question has already mentioned that the number is non negative.
- How we do this? The first idea come up with is find the pattern or rules for the result. Therefore, we can get following pattern

    ```text
    Index : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    num : 0 1 1 2 1 2 2 3 1 2 2 3 2 3 3 4
    ```

- Do you find the pattern?
- Obviously, this is overlap sub problem, and we can come up the DP solution. For now, we need find the function to implement DP.

    ```text
    dp[0] = 0;
    dp[1] = dp[0] + 1;
    dp[2] = dp[0] + 1;
    dp[3] = dp[1] +1;
    dp[4] = dp[0] + 1;
    dp[5] = dp[1] + 1;
    dp[6] = dp[2] + 1;
    dp[7] = dp[3] + 1;
    dp[8] = dp[0] + 1;
    ```

- This is the function we get, now we need find the other pattern for the function to get the general function.
- After we analyze the above function, we can get

    ```text
    dp[0] = 0;
    dp[1] = dp[1-1] + 1;
    dp[2] = dp[2-2] + 1;
    dp[3] = dp[3-2] +1;
    dp[4] = dp[4-4] + 1;
    dp[5] = dp[5-4] + 1;
    dp[6] = dp[6-4] + 1;
    dp[7] = dp[7-4] + 1;
    dp[8] = dp[8-8] + 1;
    ```

- Obviously, we can find the pattern for above example, so now we get the general function
`dp[index] = dp[index - offset] + 1;`

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/binary/counting-bits.py ':include :type=code')
<!-- tabs:end -->
