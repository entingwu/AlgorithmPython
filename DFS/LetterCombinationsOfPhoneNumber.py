from typing import List

class LetterCombinationsOfPhoneNumber:
    """
    @param digits: A digital string
    @return: all possible letter combinations
             we will sort your return value in output
    """
    KEYBOARD = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        results = []
        self.dfs(digits, 0, [], results)
        return results

    # index 当前dfs要处理digits[index]所代表的数字
    def dfs(self, digits, index, combination, results):
        if index == len(digits):
            results.append(''.join(combination))
            return

        for letter in self.KEYBOARD[digits[index]]:
            combination.append(letter)
            self.dfs(digits, index + 1, combination, results)
            combination.pop()