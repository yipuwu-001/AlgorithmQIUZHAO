#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (63.08%)
# Likes:    568
# Dislikes: 0
# Total Accepted:    164.7K
# Total Submissions: 261K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    # def levelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     if root is None:
    #         return []

    #     queue, res = [(root, 0)], []

    #     while len(queue) > 0:
    #         p, level = queue.pop(0)

    #         if level >= len(res):
    #             res.append([])

    #         res[level].append(p.val)

    #         if p.left is not None:
    #             queue.append((p.left, level+1))

    #         if p.right is not None:
    #             queue.append((p.right, level+1))
        
    #     return res

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = [] 

        def dfs(t, idx):
            if idx >= len(res):
                res.append([])
            
            res[idx].append(t.val)

            if t.left is not None:
                dfs(t.left, idx + 1)

            if t.right is not None:
                dfs(t.right, idx + 1)

        dfs(root, 0)

        return res
# @lc code=end

