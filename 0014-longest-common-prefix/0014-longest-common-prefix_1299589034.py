class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = strs[0]
        for i in range(len(common)):
            for word in strs[1:]:
                if (i == len(word)) or word[i] != common[i]:
                    return common[0:i]
        return common