#
# @lc app=leetcode.cn id=106 lang=python
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (69.07%)
# Likes:    247
# Dislikes: 0
# Total Accepted:    44K
# Total Submissions: 63.6K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(inorder) == 0 or len(postorder) == 0:
            return None

        root = TreeNode(postorder[-1])
        mid_idx = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:mid_idx], postorder[:mid_idx])
        root.right = self.buildTree(inorder[mid_idx+1:], postorder[mid_idx:-1])

        return root
# @lc code=end

# if __name__ == "__main__":
#     import print_tree

#     inorder = [9,3,15,20,7]
#     postorder = [9,15,7,20,3]
#     t = Solution().buildTree(inorder, postorder)
#     print_tree.printTree(t)