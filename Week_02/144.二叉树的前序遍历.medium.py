#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (66.25%)
# Likes:    322
# Dislikes: 0
# Total Accepted:    137.9K
# Total Submissions: 208.1K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]  
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3 
# 
# 输出: [1,2,3]
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """

    #     if root is None:
    #         return []

    #     res = []

    #     def _pre(t):
    #         if t is None:
    #             return None
            
    #         res.append(t.val)
    #         _pre(t.left)
    #         _pre(t.right)

    #     _pre(root)
    #     return res

    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """

    #     if root is None:
    #         return []

    #     stack, res = [], []

    #     stack = [root]

    #     while len(stack) > 0:
    #         root = stack.pop()
    #         res.append(root.val)

    #         if root.right is not None:
    #             stack.append(root.right)

    #         if root.left is not None:
    #             stack.append(root.left)

    #     return res

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        stack, res = [], []

        while len(stack) > 0 or root is not None:
            if root is not None:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right

        return res

# @lc code=end

