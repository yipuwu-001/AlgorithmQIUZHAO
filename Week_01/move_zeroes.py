class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        p1 = 0

        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[p1], nums[idx] = nums[idx], nums[p1]
                p1 += 1

        return  nums

