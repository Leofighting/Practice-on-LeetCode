# -*- coding:utf-8 -*-
__author__ = "leo"


# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。 


class Solution:
    def min_array(self, numbers):
        a = numbers.pop()
        while len(numbers) > 0:
            b = numbers.pop()
            if a >= b:
                a = b
            else:
                break
        return a
