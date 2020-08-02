#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (63.97%)
# Likes:    682
# Dislikes: 0
# Total Accepted:    194.6K
# Total Submissions: 303.5K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def _majority(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi-lo)//2 + lo
            left = _majority(lo, mid)
            right = _majority(mid+1, hi)

            if left == right:
                return left

            lc = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            rc = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if lc > rc else right

        return _majority(0, len(nums)-1)

# @lc code=end

