#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (36.15%)
# Likes:    457
# Dislikes: 0
# Total Accepted:    113K
# Total Submissions: 311.7K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 
# 
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 
# 
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 说明:
# 
# 
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
# 
# 
#

# @lc code=start
class Solution(object):
    # def _pow(self, x, n):
    #     # terminal
    #     if n == 0:
    #         return 1.0

    #     # split subproblems
    #     n1 = n/2

    #     #drill down and conquer subproblems
    #     tmp = self._pow(x, n1)

    #     #merge subproblems results
    #     result = None 
    #     if n % 2 == 0:
    #         result = tmp * tmp
    #     else:
    #         result = tmp * tmp * x
        
    #     # revert the current level states
    #     # pass, do nothing

    #     return result

    def _pow(self, x, n):
        ans = 1.0

        x_contrbute = x

        while n > 0:
            if n %  2 == 1:
                ans *= x_contrbute
            
            x_contrbute *= x_contrbute

            n //= 2

        return ans

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1.0 / x
            n *= -1
        
        return self._pow(x, n)
        
# @lc code=end

