#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#
# https://leetcode-cn.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (75.87%)
# Likes:    504
# Dislikes: 0
# Total Accepted:    98.5K
# Total Submissions: 129.8K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# 翻转一棵二叉树。
# 
# 示例：
# 
# 输入：
# 
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
# 
# 输出：
# 
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
# 
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
# 
# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return root
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    # dfs_pre
    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """

    #     if root is None:
    #         return root
        
    #     head = root

    #     stack = [root]

    #     while len(stack) > 0:
    #         root = stack.pop()

    #         root.left, root.right = root.right, root.left

    #         if root.left is not None:
    #             stack.append(root.left)

    #         if root.right is not None:
    #             stack.append(root.right)
        
    #     return head

    #  dfs_pre_v1
    #  def invertTree(self, root):
    #      """
    #      :type root: TreeNode
    #      :rtype: TreeNode
    #      """

    #      if root is None:
    #          return root
       
    #      head = root

    #      stack = []

    #      while len(stack) > 0 or root is not None:
    #         if root is not None:
    #             stack.append(root)
    #             root.left, root.right = root.right, root.left
    #             root = root.left
    #         else:
    #             root = stack.pop()
    #             root = root.right
       
    #      return head


# if __name__ == "__main__":
#      import util
#      import create
#      arr = [3,9,20,None,None,15,7]
#      arr = [4,2,7,1,3,6,9]
#      t = create.pre(arr)
#      print(util.dfs_pre(t))

#      Solution().invertTree(t)

#      print(util.dfs_pre(t))

# @lc code=end

