#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (61.35%)
# Likes:    622
# Dislikes: 0
# Total Accepted:    127K
# Total Submissions: 206.9K
# Testcase Example:  '3\n2'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 问总共有多少条不同的路径？
# 
# 
# 
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
# 
# 
# 
# 示例 1:
# 
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 
# 
# 示例 2:
# 
# 输入: m = 7, n = 3
# 输出: 28
# 
# 
# 
# 提示：
# 
# 
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10 ^ 9
# 
# 
#

# @lc code=start
class Solution(object):
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     # 重复性 分治思想， 
    #     #1. f(i, j) = f(i+1, j) + f(i, j+1)
    #     #2. 中间状态：dp[[]]
    #     # 3. dp方程： f(i, j) = f(i+1, j) + f(i, j+1)

    #     dp = [[0] *(n-1) +[1] for _ in range(m-1)] + [[1] * n]

    #     for i in range(m - 2, -1, -1):
    #         for j in range(n - 2, -1, -1):
    #             dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
    #     return dp[0][0]

    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     # 重复性 分治思想， 
    #     #1. f(i, j) = f(i+1, j) + f(i, j+1)
    #     #2. 中间状态：dp[[]]
    #     # 3. dp方程： f(i, j) = f(i+1, j) + f(i, j+1)

    #     dp = [1] * n

    #     for _ in range(m - 2, -1, -1):
    #         for j in range(n - 2, -1, -1):
    #             dp[j] += dp[j+1]
        
    #     return dp[0]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        return dp[-1]



# @lc code=end

