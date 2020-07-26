#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (64.69%)
# Likes:    667
# Dislikes: 0
# Total Accepted:    102.8K
# Total Submissions: 158.7K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 
# 
# 示例 2:
# 
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 
# 
# 说明:
# 
# 
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
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
    # ans = None

    # def dfs(self, root, p, q):
    #     if root is None:
    #         return root
        
    #     fl = self.dfs(root.left, p, q)
    #     fr = self.dfs(root.right, p, q)

    #     if fl and fr or ((fl or fr) and (root.val == p.val or root.val == q.val)):
    #         self.ans = root

    #     return  fl or  fr or root.val == p.val or root.val == q.val

    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """

    #     self.dfs(root, p, q)
    #     return self.ans


    def dfs(self, root, parrent):
        if root is None:
            return

        if root.left is not None:
            parrent[root.left.val] = root
            self.dfs(root.left, parrent)

        if root.right is not None:
            parrent[root.right.val] = root
            self.dfs(root.right, parrent)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return root

        visted = {}
        parrent = {}

        self.dfs(root, parrent)
        parrent[root.val] = None

        while p is not None:
            visted[p.val] = 1
            p = parrent[p.val]
        

        while q is not None:
            if q.val in visted:
                return q

            q = parrent[q.val]
        
        return None
        
# @lc code=end