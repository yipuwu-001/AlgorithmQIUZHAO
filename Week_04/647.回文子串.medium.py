#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (62.11%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    35.4K
# Total Submissions: 56.8K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
# 
# 示例 1:
# 
# 
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
# 
# 
# 示例 2:
# 
# 
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 注意:
# 
# 
# 输入的字符串长度不会超过1000。
# 
# 
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        
        m = len(s)
        dp = [[0] * m for _ in range(m)]

        for i in range(m):
            dp[i][i] = 1

        num = m

        for i in range(m-1, -1, -1):
            for j in range(i+1, m):
                if s[i] == s[j]:
                    if(j-i) == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 0
                
                if dp[i][j] == 1:
                    num += 1

        return num

                    

        
# @lc code=end

