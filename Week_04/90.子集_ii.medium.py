#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (60.54%)
# Likes:    285
# Dislikes: 0
# Total Accepted:    42.5K
# Total Submissions: 70.2K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        n = len(nums)

        nums = sorted(nums)

        def dfs(path, start):
            ans.append(path)

            for idx in range(start, n):
                if idx > start and nums[idx-1] == nums[idx]:
                    continue

                dfs(path + [nums[idx]], idx + 1)
        dfs([], 0)
        return ans
# @lc code=end

