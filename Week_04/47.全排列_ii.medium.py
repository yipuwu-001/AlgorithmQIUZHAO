#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (59.45%)
# Likes:    368
# Dislikes: 0
# Total Accepted:    76.9K
# Total Submissions: 129.3K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        nums = sorted(nums)

        def dfs(path, start, used):
            if start == len(nums):
                ans.append(path)
                return
            
            for idx, num in enumerate(nums):
                if used[idx]:
                    continue

                # 这里为什么需要not used[idx-1], 有2中情况:
                # nums: [1, 1', 2]
                #              []
                #           /      \ case1
                #          1        1'
                #   case2 /  \    /    \
                #       1'    2  1      2
                # 对于case1中的 1' 是需要裁剪掉的, 因为1'子树和1子树产生的序列完全一样, 但由于恢复撤销导致used[idx-1] == false
                # 对于case2中的 1' 是不能裁剪掉的, 因为是不同层次的重复, [1, 1', 2]是一个合法的排列, 此时used[idx-1] == true
                # 所以需要判断used[idx-1] ==fase的裁剪掉
                if idx > 0 and nums[idx-1] == num and not used[idx -1]:
                    print("continue right")
                    continue

                used[idx] = True
                dfs(path+[num], start + 1, used)
                used[idx] = False
        
        dfs([], 0, [False] * len(nums))
        return ans
# @lc code=end

