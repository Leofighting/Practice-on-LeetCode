# -*- coding:utf-8 -*-
__author__ = "leo"

# 输入整数数组 arr ，找出其中最小的 k 个数。
# 例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。


import heapq


class Solution:
    def get_least_number(self, arr, k):
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]

        heapq.heapify(hp)

        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


class Solution1:
    def get_least_number(self, arr, k):
        return sorted(arr)[:k]


