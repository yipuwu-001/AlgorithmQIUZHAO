#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (72.13%)
# Likes:    587
# Dislikes: 0
# Total Accepted:    195.8K
# Total Submissions: 271.4K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
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
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """

    #     res = []

    #     def recurse(t):
    #         if t is None:
    #             return []
            
    #         recurse(t.left)
    #         res.append(t.val)
    #         recurse(t.right)
        
    #     recurse(root)

    #     return res

    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """

    #     if root is None:
    #         return []

    #     stack, res = [], []

    #     while len(stack) > 0 or root is not None:
    #         if root is not None:
    #             stack.append(root)
    #             root = root.left
    #         else:
    #             root = stack.pop()
    #             res.append(root.val)
    #             root = root.right
            
    #     return res
        
     def inorderTraversal(self, root):
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
                 root = root.left
             else:
                 root = stack.pop()
                 res.append(root.val)
                 root = root.right
           
         return res

# @lc code=end

