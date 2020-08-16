#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 朋友圈
#
# https://leetcode-cn.com/problems/friend-circles/description/
#
# algorithms
# Medium (57.69%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    57.9K
# Total Submissions: 100.2K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j
# 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
# 
# 
# 
# 示例 1：
# 
# 输入：
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# 输出：2 
# 解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回 2 。
# 
# 
# 示例 2：
# 
# 输入：
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# 输出：1
# 解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1
# 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 200
# M[i][i] == 1
# M[i][j] == M[j][i]
# 
# 
#

# @lc code=start

class UionFind():
    def __init__(self, n):
        self.count = n
        self.parent = [idx for idx in range(n)]
    
    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        
        return i
    
    def uion(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return root_p
        
        self.parent[root_p] = root_q
        self.count -= 1

        return root_q
    
class Solution(object):
    # def findCircleNum(self, M):
    #     """
    #     :type M: List[List[int]]
    #     :rtype: int
    #     """

    #     num = len(M)
    #     visted = [0] * num
    #     count = 0

    #     def _dfs(idx):
    #         for j in range(num):
    #             if M[idx][j] == 1 and not visted[j]:
    #                 visted[j] = 1
    #                 _dfs(j)
        
    #     for i in range(num):
    #         if not visted[i]:
    #             _dfs(i)
    #             count += 1
        
    #     return count

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        num = len(M)
        if num == 0:
            return 0
        
        uf = UionFind(num)

        for i in range(num):
            for j in range(num):
                if M[i][j] == 1:
                    uf.uion(i, j)

        return uf.count


# @lc code=end
