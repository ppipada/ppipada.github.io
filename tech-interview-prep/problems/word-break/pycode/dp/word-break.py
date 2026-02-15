class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i:j + 1] in wordDict:
                        dp[j + 1] = True

        return dp[-1]
