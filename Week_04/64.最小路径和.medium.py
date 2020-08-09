#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (67.38%)
# Likes:    616
# Dislikes: 0
# Total Accepted:    132.4K
# Total Submissions: 196.2K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
class Solution(object):
    # def minPathSum(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     m, n = len(grid), len(grid[-1])
    #     dp = [[0] * n for _  in range(m)]

    #     # base case, init first row
    #     # i, j == 0
    #     dp[0][0] = grid[0][0]

    #     # i == 0, j != 0
    #     for j in range(1, n):
    #         dp[0][j] = dp[0][j-1] + grid[0][j]

    #     # i != 0, j == 0
    #     for i in range(1, m):
    #         dp[i][0] = dp[i-1][0] + grid[i][0]

    #     for i in range(1, m):
    #         for j in range(1, n):
    #             # i != 0, j != 0
    #             dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
    #     return dp[-1][-1]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[-1])

        # base case, init first row
        dp = [grid[0][0]] * n

        # i == 0, j != 0
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]

        for i in range(1, m):
            dp[0] += grid[i][0]

            for j in range(1, n):
                # i != 0, j != 0
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        
        return dp[-1]
# @lc code=end

