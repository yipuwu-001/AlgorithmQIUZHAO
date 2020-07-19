import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = collections.defaultdict(list)

        int_a = ord("a")

        for elm in strs:
            counter = [0] * 26

            for ch in elm:
                counter[ord(ch) - int_a] += 1

            key = "".join([str(n) for n in counter])
            ans[key].append(elm)

        return ans.values()

print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
