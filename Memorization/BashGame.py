class BashGame:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n: int) -> bool:
        return self.memo_search(n, {})

    def memo_search(self, n, memo):
        if n <= 3:
            return True
        if n in memo:
            return memo[n]

        for i in range(1, 4):
            if not self.memo_search(n - i, memo): # 后手相反
                memo[n] = True
                return True
        memo[n] = False
        return False

    def can_win_bash_1(self, n: int) -> bool:
        if n <= 3:
            return True
        for i in range(1, n):
            if not self.can_win_bash(n - i): # 后手
                return True
        return False