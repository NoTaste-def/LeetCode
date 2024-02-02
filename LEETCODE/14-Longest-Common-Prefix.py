class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        strs.sort()

        first = strs[0]
        last = strs[-1]

        for i in range(len(strs[0])):
            if last[i] == first[i]:
                result += first[i]
            else:
                break
        return result 