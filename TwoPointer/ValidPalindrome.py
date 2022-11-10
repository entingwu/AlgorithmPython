class ValidPalindrome:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def is_valid(self, char):
        return char.isdigit() or char.isalpha()


    """
    Valid Palindrome II
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s: str) -> bool:
        if not s:
            return True
        left, right = self.find_difference(s, 0, len(s) - 1)
        if left >= right:
            return True
        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)

    def find_difference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        return left, right

    def is_palindrome(self, s, left, right):
        left, right = self.find_difference(s, left, right)
        return left >= right
