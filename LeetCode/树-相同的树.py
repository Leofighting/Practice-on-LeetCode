# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree(p.right, q.right) and self.is_same_tree(p.left, q.left)
