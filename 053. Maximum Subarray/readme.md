## [53. Maximum Subarray](https://leetcode-cn.com/problems/maximum-subarray/)

### 题目描述

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

```
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

### 思路

遍历到第k个数的时候，如果前k-1个数之和为负数，则丢弃前k-1个数之和。遍历过程中保存最大和。