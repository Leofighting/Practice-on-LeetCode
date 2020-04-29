# -*- coding:utf-8 -*-
__author__ = "leo"


# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。


class Solution:
    def num_way(self, n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
