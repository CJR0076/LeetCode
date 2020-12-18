## [136. Single Number](https://leetcode-cn.com/problems/single-number/)

### 题目描述
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

```
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
```

### 思路

第一次知道异或找到这个元素时还很兴奋，现在已经是老生常谈了，两个相同的元素异或后变成0，根据这个得到代码
