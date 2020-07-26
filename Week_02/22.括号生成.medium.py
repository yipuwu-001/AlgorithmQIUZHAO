#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (75.85%)
# Likes:    1192
# Dislikes: 0
# Total Accepted:    153.9K
# Total Submissions: 202.9K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        res = []

        def _gen(left, right, m, bstr):
            if len(bstr) == 2 * m:
                res.append(bstr)
                return
            
            if left < n:
                _gen(left + 1, right, m , bstr + "(")
            
            if right < left:
                _gen(left, right + 1, m , bstr + ")")


        _gen(0, 0, n, "")
        return res

# @lc code=end

