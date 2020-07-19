class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = 0

        for idx in range(len(digits)-1, -1, -1):
            val = (digits[idx] + 1)
            digits[idx] = val % 10
            tmp = val // 10

            if tmp == 0:
                return digits

        if tmp > 0:
            digits.insert(0, tmp)

        return digit
