#
# @lc app=leetcode.cn id=137 lang=python
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (67.59%)
# Likes:    391
# Dislikes: 0
# Total Accepted:    37.4K
# Total Submissions: 55.3K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,3,2]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
# 
#

# @lc code=start
class Solution:
    # def singleNumber(self, nums):

    #     counts = [0] * 32

    #     for num in nums:
    #         for j in range(32):
    #             counts[j] += num & 1
    #             num >>= 1

    #     res, m = 0, 3

    #     for i in range(32):
    #         res <<= 1
    #         res |= counts[31 - i] % m

    #     return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)

    def singleNumber(self, nums):
        ones, twos = 0, 0 

        for num in nums:
            ones = ones ^ num & ~ twos
            twos = twos ^ num & ~ ones
        
        return ones

# @lc code=end
