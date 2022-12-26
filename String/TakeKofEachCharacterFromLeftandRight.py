import collections
class TakeKofEachCharacterFromLeftandRight:
    def takeCharacters(self, s: str, k: int) -> int:
        n, res = len(s), float('inf')
        char_to_cnt = collections.defaultdict(int)
        char_to_cnt["a"] = 0
        char_to_cnt["b"] = 0
        char_to_cnt["c"] = 0
        for char in s:
            char_to_cnt[char] = char_to_cnt.get(char, 0) + 1
        print(char_to_cnt)
        for char in char_to_cnt:
            if char_to_cnt[char] < k:
                return -1

        # 移除s[i], 加入s[j], 使得(i-j+1)为扣掉的一段
        j = 0
        for i in range(n):
            cur = s[i]
            char_to_cnt[cur] = char_to_cnt.get(cur, 0) - 1
            if char_to_cnt[cur] == 0:
                del char_to_cnt[cur]
            while j <= i and not self.isValid(char_to_cnt, k):
                char = s[j]
                char_to_cnt[char] = char_to_cnt.get(char, 0) + 1
                j += 1

            res = min(n - (i - j + 1), res)
            print(j, i, res, char_to_cnt)
        return res if res >= 0 else -1

    # valid means >=2a, >=2b, >=2c
    def isValid(self, counter, k):
        if counter.get("a", 0) < k or counter.get("b", 0) < k or counter.get("c", 0) < k:
            return False
        return True