# -*- coding:utf-8 -*-
__author__ = "leo"


# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。


class Solution:
    def missing_number(self, nums):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1

        return i


class Solution1:
    def missing_number(self, nums):
        n = len(nums)
        return int(n * (n + 1) / 2 - sum(nums))
