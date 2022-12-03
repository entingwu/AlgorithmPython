class WildcardMatching:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        memo = [[None] * len(p) for _ in range(len(s))]
        return self.is_match_helper(s, 0, p, 0, memo)

    def is_match_helper(self, source, s_idx, pattern, p_idx, memo):
        if len(pattern) == p_idx:
            return len(source) == s_idx

        if len(source) == s_idx:
            return self.all_star(pattern, p_idx)

        if memo[s_idx][p_idx] is not None:
            return memo[s_idx][p_idx]

        s_char = source[s_idx]
        p_char = pattern[p_idx]

        is_match = False
        if p_char == '*':
            is_match = self.is_match_helper(source, s_idx + 1, pattern, p_idx, memo) or self.is_match_helper(source, s_idx, pattern, p_idx + 1, memo)
        else:
            is_match = self.is_match_char(s_char, p_char) and self.is_match_helper(source, s_idx + 1, pattern, p_idx + 1, memo)

        memo[s_idx][p_idx] = is_match
        return memo[s_idx][p_idx]

        # if p_char != '*':
        #     return self.is_match_char(s_char, p_char) and self.is_match_helper(source, s_idx + 1, pattern, p_idx + 1)
        #
        # for i in range(s_idx, len(source) + 1):
        #     if self.is_match_helper(source, i, pattern, p_idx + 1):
        #         return True
        # return False

    def is_match_char(self, s_char, p_char):
        return (s_char == p_char) or (p_char == '?')

    def all_star(self, pattern, p_idx):
        for i in range(p_idx, len(pattern)):
            if pattern[i] != '*':
                return False
        return True
