# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个整数数组，判断是否存在重复元素。
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。


class Solution:
    def contains_duplicate(self, nums):
        return len(nums) > len(set(nums))


class Solution1:
    def contains_duplicate(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
