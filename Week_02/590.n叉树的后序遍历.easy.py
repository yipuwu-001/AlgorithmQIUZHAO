#
# @lc app=leetcode.cn id=590 lang=python
#
# [590] N叉树的后序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (73.98%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    29.6K
# Total Submissions: 39.9K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的后序遍历。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其后序遍历: [5,6,3,2,4,1].
# 
# 
# 
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?
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
    #  def postorder(self, root):
    #     """
    #     :type root: Node
    #     :rtype: List[int]
    #     """
    #     if root is None:
    #         return []
        
    #     res = []

    #     def _post(t):
    #         if t is None:
    #             return None
            
    #         for ch in t.children:
    #             if ch is not None:
    #                 _post(ch)
            
    #         res.append(t.val)
        
    #     _post(root)
    #     return res


    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if root is None:
            return []
        
        stack, res = [root], []

        while len(stack) > 0:
            root = stack.pop()

            res.append(root.val)

            for ch in root.children:
                if ch is not None:
                    stack.append(ch)

        return res[::-1]

        
# @lc code=end

