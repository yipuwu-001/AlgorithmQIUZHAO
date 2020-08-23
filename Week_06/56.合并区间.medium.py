#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (42.82%)
# Likes:    571
# Dislikes: 0
# Total Accepted:    133.9K
# Total Submissions: 311.9K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 
# 
# 示例 1:
# 
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
# 
# 
# 
# 提示：
# 
# 
# intervals[i][0] <= intervals[i][1]
# 
# 
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals = sorted(intervals, key=lambda it: it[0])

        merged = []

        for (start, end) in intervals:
            if len(merged) == 0 or merged[-1][1] < start:
                merged.append([start, end])
            else:
                pre_start, prev_end = merged[-1]
                merged[-1] = [min(pre_start, start), max(prev_end, end)]
        
        return merged

# @lc code=end

