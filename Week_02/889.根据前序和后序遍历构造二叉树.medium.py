#
# @lc app=leetcode.cn id=889 lang=python
#
# [889] 根据前序和后序遍历构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (65.55%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 8.9K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# 返回与给定的前序和后序遍历匹配的任何二叉树。
# 
# pre 和 post 遍历中的值是不同的正整数。
# 
# 
# 
# 示例：
# 
# 输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= pre.length == post.length <= 30
# pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
# 每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
# 
# 
#

#ref: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/solution/tu-jie-889-gen-ju-qian-xu-he-hou-xu-bian-li-gou-2/

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        if len(preorder) == 0 or len(postorder) == 0:
            return None
        
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        mid_idx = postorder.index(preorder[1])

        root.left = self.constructFromPrePost(preorder[1:mid_idx+2], postorder[:mid_idx+1])
        root.right = self.constructFromPrePost(preorder[mid_idx+2:], postorder[mid_idx+1:-1])

        return root
        
# @lc code=end

# if __name__ == "__main__":
#     preorder = [1,2,4,5,3,6,7]
#     postoreder = [4,5,2,6,7,3,1]

#     t = Solution().constructFromPrePost(preorder, postoreder)
#     import print_tree
#     print_tree.printTree(t)
