class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_len = len(nms)
        k %= num_len

        self.reverse(nums, 0, num_len-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, num_len-1)

        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
