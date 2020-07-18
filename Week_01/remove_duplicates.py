# coding: utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        p1 = 0

        for p2 in range(1, len(nums)):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]

        return p1 + 1


if __name__ == "__main__":
    arr = [1,1,2]

    len = Solution().removeDuplicates(arr)
    assert arr[:len] == [1,2]
