import collections
from typing import List

class FindTheMaximumDivisibilityScore:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        score_to_divisors = collections.defaultdict(list)
        max_score, min_divisor = 0, 0
        for idx, divisor in enumerate(divisors):
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            score_to_divisors[score].append(divisor)
            if score > max_score:
                max_score = score
        divisors_list = score_to_divisors[max_score]
        return min(divisors_list)

    def addMinimum(self, word: str) -> int:
        print(word)
        expect = "a"
        cnt = 0
        for idx, ch in enumerate(word):
            if ch == expect:
                expect = chr(ord("a") + (ord(expect) - ord("a") + 1) % 3)
                print("^", idx, ch, expect)
                continue
            else:
                num = ord(ch) - ord(expect)
                print("*", idx, ch, expect)
                cnt += num + 3 if num < 0 else num
                expect = chr(ord("a") + (ord(ch) - ord("a") + 1) % 3)
                print("#", idx, cnt, expect)
        print("@", expect, word[-1], cnt)
        # last one
        expect = "c"
        if word[-1] != expect:
            num = ord(expect) - ord(word[-1])
            cnt += num + 3 if num < 0 else num
        return cnt
