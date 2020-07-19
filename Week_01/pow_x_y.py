class Solution(object):
    def powxy(self, x, y):

        if y == 0:
            return 1

        v = self.powxy(x, y // 2)

        if y % 2 == 1:
            return v * v * x

        return v * v


print Solution().powxy(2, 3)
