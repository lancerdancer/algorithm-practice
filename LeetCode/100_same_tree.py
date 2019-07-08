"""
Link: https://leetcode.com/problems/same-tree/
Solution by Yongxu Yao
"""
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Recursive solution
    def isSameTree_iter(self, p: TreeNode, q: TreeNode) -> bool:

        if p is None and q is None:
            return True

        elif p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree_iter(p.left, q.left) and self.isSameTree_iter(p.right, q.right)

    # Iterative solution
    def isSameTree_rec(self, p: TreeNode, q: TreeNode):

        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])

        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True


