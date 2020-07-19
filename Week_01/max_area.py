class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0

        if len(height) == 0:
            return 0

        left, right = 0, len(height) - 1

        while left < right:

            min_height = min(height[left], height[right])

            max_area = max(min_height * (right - left), max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_are
