#
# @lc app=leetcode.cn id=429 lang=python
#
# [429] N叉树的层序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (66.01%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    25.2K
# Total Submissions: 38.2K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其层序遍历:
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
# 
# 
# 
# 说明:
# 
# 
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    # def levelOrder(self, root):
    #     """
    #     :type root: Node
    #     :rtype: List[List[int]]
    #     """
    #     if root is None:
    #         return []
        
    #     res = []

    #     def _dfs(t, lvl):
    #         if lvl >= len(res):
    #             res.append([])

    #         res[lvl].append(t.val)

    #         for ch in t.children:
    #             if ch is not None:
    #                 _dfs(ch, lvl + 1)
            
    #     _dfs(root, 0)
    #     return res

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        if not root:
             return []

        queue = [root]
        res = []

        while queue:
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return res

        
# @lc code=end