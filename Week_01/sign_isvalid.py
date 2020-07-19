class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        ans = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
        }
        for ch in s:
            if ch in ans:
                if len(stack) == 0:
                    return False

                if ans.get(ch) != stack.pop():
                    return False
            else:
                stack.append(ch)

        return len(stack) == 
