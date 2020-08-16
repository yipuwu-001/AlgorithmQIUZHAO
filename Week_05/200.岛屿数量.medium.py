#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.06%)
# Likes:    707
# Dislikes: 0
# Total Accepted:    142.9K
# Total Submissions: 285.5K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1:
# 
# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
# 
# 
#

# @lc code=start

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        num_x = len(grid)
        if num_x == 0:
            return 0

        count = 0
        num_y = len(grid[0])
        
        def _dfs(x, y):
            grid[x][y] = "0"

            for i, j in [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1)]:

                if (i >= 0 and i < num_x 
                    and j >= 0 and j < num_y
                    and grid[i][j] == "1"):
                    _dfs(i, j)
        
        for i in range(num_x):
            for j in range(num_y):
                if grid[i][j] == "1":
                    _dfs(i, j)
                    count += 1
        
        return count

# @lc code=end

