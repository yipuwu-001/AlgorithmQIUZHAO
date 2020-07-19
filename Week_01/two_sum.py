class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cached = {}

        for idx, val in enumerate(nums):
            comp = target - val
            if comp in cached:
                return cached[comp], idx

            cached[val] = idx

        return None, None
