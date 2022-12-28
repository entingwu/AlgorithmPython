class DistinctSubsequences:
    """
    @param s: The string s
    @return: The number of distinct, non-empty subsequences of S.
    """
    MOD = 10 ** 9 + 7
    def distinct_subseq_i_i(self, s: str) -> int:
        n = len(s)
        # state: dp[i]表示以下标i作为subsequence的最后一个字符的方案总数
        dp = [0] * n
        # initialize: 如果i是第一个出现s[i]这个字符的位置，那么dp[i] = 1
        visited = set()
        for i in range(n):
            if s[i] not in visited:
                dp[i] = 1
            visited.add(s[i])

        # function
        for i in range(n):
            for j in range(i - 1, -1, -1):
                dp[i] = (dp[i] + dp[j]) % self.MOD
                if s[i] == s[j]:
                    break
        print(dp)
        # answer: 以所有位置结尾的方案总数之和
        return sum(dp) % self.MOD
