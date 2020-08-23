#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (46.30%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    95K
# Total Submissions: 204K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 
# 
# 示例：
# 
# s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
# 
# 
# 
# 
# 提示：你可以假定该字符串只包含小写字母。
# 
#

# @lc code=start
from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx

        return -1

# @lc code=end

