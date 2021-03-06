# -*- coding:utf-8 -*-
__author__ = "leo"


# 使用队列实现栈的下列操作：
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空

import collections


class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        pop = self.stack[-1]
        self.stack.remove(pop)
        return pop

    def top(self):
        return self.stack[-1]

    def empty(self):
        return True if len(self.stack) == 0 else False


class MyStack1:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, x):
        self.queue.append(x)
        l = len(self.queue)
        for _ in range(l-1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return not self.queue
