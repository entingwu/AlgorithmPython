
class LongestPalindromeSubstring:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    # 相向双指针
    """
    def longest_palindrome(self, s: str) -> str:
        if not s:
            return ""
        for length in range(len(s), 0, -1):
            for i in range(0, len(s) - length + 1):
                l, r = i, i + length - 1
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:
                    return s[i: i + length]
        return ""

    # Dynamic Programming
    def longest_palindrome_3(self, s: str) -> str:
        if not s:
            return ""
        # initialize
        n = len(s)
        F = [[False] * n for _ in range(n)]
        for i in range(n):
            F[i][i] = True
        for i in range(1, n):
            F[i][i - 1] = True

        # function
        start, longest = 0, 1
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                F[i][j] = F[i + 1][j - 1] and (s[i] == s[j])
                if F[i][j] and length > longest:
                    longest = length
                    start = i
        return s[start: start + longest]

    # 背向双指针
    def longest_palindrome_2(self, s: str) -> str:
        if not s:
            return ""

        answer = (0, 0) # start, longest
        for mid in range(len(s)):
            answer = max(answer, self.get_palindrome_from(s, mid, mid))
            answer = max(answer, self.get_palindrome_from(s, mid, mid + 1))
        return s[answer[1]: answer[0] + answer[1]]

    def get_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, left + 1

    def longest_palindrome_1(self, s: str) -> str:
        if not s:
            return ""

        start, longest = 0, 0
        for mid in range(0, len(s)):
            # odd
            left, right = mid, mid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > longest:
                longest = right - left - 1
                start = left + 1  # s[left] != s[right]

            # even
            left, right = mid, mid + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > longest:
                longest = right - left - 1
                start = left + 1

        return s[start: start + longest]
