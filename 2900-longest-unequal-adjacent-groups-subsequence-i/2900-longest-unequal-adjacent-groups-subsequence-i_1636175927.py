class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        num = len(groups)
        answer = [words[0]]
        last_group = groups[0]
        for i in range(1, num):
            if groups[i] != last_group:
                answer.append(words[i])
                last_group = groups[i]
        return answer

        