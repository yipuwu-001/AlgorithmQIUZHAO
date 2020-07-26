#
# @lc app=leetcode.cn id=239 lang=python
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (48.37%)
# Likes:    457
# Dislikes: 0
# Total Accepted:    61.7K
# Total Submissions: 127.5K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 
# 返回滑动窗口中的最大值。
# 
# 
# 
# 进阶：
# 
# 你能在线性时间复杂度内解决此题吗？
# 
# 
# 
# 示例:
# 
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
# ⁠ 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
     def maxSlidingWindow(self, nums,  k):
         # base cases
         n = len(nums)
         if n * k == 0:
             return []

         if k == 1:
             return nums
    
         deq, res = deque(), []

         for idx in range(n):
             # remove the outwindow element
             if len(deq) > 0 and idx - deq[0] + 1 > k:
                 deq.popleft()
           
             # remote left than nums[idx] in deq
             while len(deq) > 0 and nums[deq[-1]] <= nums[idx]:
                 deq.pop()

             deq.append(idx)

             # append max value
             if idx + 1 >= k:
                 res.append(nums[deq[0]])
           
         return res
# @lc code=end

