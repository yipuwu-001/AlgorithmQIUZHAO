#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (71.96%)
# Likes:    350
# Dislikes: 0
# Total Accepted:    98.8K
# Total Submissions: 137.2K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [], []

        while len(stack) > 0 or root is not None:
            if root is not None:
                stack.append((root, 0))
                root = root.left
            else:
                root, visted = stack.pop()

                if visted == 0:
                    stack.append((root, 1))
                    root = root.right
                else:
                    res.append(root.val)
                    root = None
        
        return res

# @lc code=end

