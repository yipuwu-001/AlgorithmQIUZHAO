class Solution(object):
   #def climbStairs(self, n):
   #    """
   #    :type n: int
   #    :rtype: int
   #    """
   #    if n <= 2:
   #        return n
   #    return self.climbStairs(n - 1) + self.climbStairs(n-2)

   # def climbStairs(self, n):
   #     """
   #     :type n: int
   #     :rtype: int
   #     """
   #     if n <= 2:
   #         return n
   #
   #     f1, f2 = 1, 2
   #
   #     counts = 0
   #     for x in range(3, n+1):
   #         counts = f1 + f2
   #         f1 = f2
   #         f2 = counts
   #
   #     return counts

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = math.sqrt(5)
        fibn = math.pow((1 + x)/2, n + 1) - math.pow((1 - x)/2, n + 1)

        return int(fibn/x)
