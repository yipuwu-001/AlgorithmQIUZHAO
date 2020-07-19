class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = [0] * 26

        int_a = ord("a")
        for ch in s:
            counter[ord(ch) - int_a] += 1

        for ch in t:
            counter[ord(ch) - int_a] -= 1

        for c in counter:
            if c != 0:
                return False

        return Tru
