#
# @lc app=leetcode.cn id=493 lang=python
#
# [493] 翻转对
#
# https://leetcode-cn.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (27.60%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 23.2K
# Testcase Example:  '[1,3,2,3,1]'
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
# 
# 你需要返回给定数组中的重要翻转对的数量。
# 
# 示例 1:
# 
# 
# 输入: [1,3,2,3,1]
# 输出: 2
# 
# 
# 示例 2:
# 
# 
# 输入: [2,4,3,5,1]
# 输出: 3
# 
# 
# 注意:
# 
# 
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。
# 
# 
#

# @lc code=start
class Solution(object):
    def merge(self, nums, left, mid, right):
        i, j = left, mid + 1

        ans = 0

        while(i <= mid and j <= right):
            if nums[i] > 2 * nums[j]:
                ans += (mid - i + 1)
                j += 1
            else:
                i += 1

        tmp = []
        i, j = left, mid + 1
        while(i <= mid and j <= right):
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        
        while(i <= mid):
            tmp.append(nums[i])
            i += 1

        while(j <= right):
            tmp.append(nums[j])
            j += 1

        nums[left:right+1] = tmp

        return ans

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _merge(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) >> 1
            l_cnt = _merge(left, mid)
            r_cnt = _merge(mid + 1, right)

            return self.merge(nums, left, mid, right) + l_cnt + r_cnt
        
        return _merge(0, len(nums)-1)
        
# @lc code=end

