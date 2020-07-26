#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (73.82%)
# Likes:    612
# Dislikes: 0
# Total Accepted:    212.9K
# Total Submissions: 288.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # def maxDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if root is None:
    #         return 0

    #     max_h = 0

    #     stack = [(root, 1)]

    #     while len(stack) > 0:
    #         root, h = stack.pop()

    #         max_h = max(max_h, h)

    #         if root.left is not None:
    #             stack.append((root.left, h + 1))

    #         if root.right is not None:
    #             stack.append((root.right, h + 1))
        
    #     return max_h
    

# if __name__ == "__main__":
#      import util
#      import create
#      arr = [3,9,20,None,None,15,7]
#      t = create.pre(arr)
#      print(Solution().maxDepth(t))

# @lc code=end

