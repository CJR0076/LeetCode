## [78. Subsets](https://leetcode-cn.com/problems/subsets/)

### 题目描述

Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
```
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
```

### 思路

1.先取空列表[]加入res，res = [[]]
2.然后把[] + nums[0]加进去，res = [[], [1]]
3.把[] + nums[1], [1] + nums[1]加进去，res = [[], [1], [2], [1, 2]]
4.[] + nums[2], [1] + nums[2], [2] + nums[2], [1, 2] + nums[2]，res = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
5.完毕，基本思路就是每次把res的值都取出来加入新元素再放进去，等于是一个双循环
