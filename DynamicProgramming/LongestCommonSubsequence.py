class LongestCommonSubsequence:
    """
    @param a: A string
    @param b: A string
    @return: The length of longest common subsequence of A and B
    """
    def longest_common_subsequence(self, a: str, b: str) -> int:
        if not a or not b:
            return 0
        len_a, len_b = len(a), len(b)
        # state
        dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

        # function
        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if a[i - 1] == b[i - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len_a][len_b]
