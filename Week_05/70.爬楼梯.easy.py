#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (50.06%)
# Likes:    1145
# Dislikes: 0
# Total Accepted:    245.3K
# Total Submissions: 489.9K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#

# @lc code=start
import math

class Solution(object):
   #def climbStairs(self, n):
   #    """
   #    :type n: int
   #    :rtype: int
   #    """
   #    if n <= 2:
   #        return n
   #    return self.climbStairs(n - 1) + self.climbStairs(n-2)

    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     x = math.sqrt(5)
    #     fibn = math.pow((1 + x)/2, n + 1) - math.pow((1 - x)/2, n + 1)

    #     return int(fibn/x)

    # dp
   def climbStairs(self, n):
       """
       :type n: int
       :rtype: int
       """
       # 0 ,1, 2, 3
       # 0, 1, 2, 3
       if n <= 2:
           return n
   
       f1, f2 = 1, 2
   
       for _ in range(3, n+1):
           f1, f2 = f2, f1+f2
   
       return f2

# @lc code=end

