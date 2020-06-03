# -*- coding:utf-8 -*-
__author__ = "leo"


# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
# 注意：整数序列中的每一项将表示为一个字符串。


class Solution:
    def count_and_say(self, n):
        prev = [1]
        for i in range(1, n):
            new = []
            count = 1
            p = None
            for ele in prev:
                if p is None:
                    p = ele
                elif ele == p:
                    count += 1
                else:
                    new.extend([count, p])
                    p = ele
                    count = 1
            new.extend([count, p])
            prev = new
        return "".join([str(num) for num in prev])
