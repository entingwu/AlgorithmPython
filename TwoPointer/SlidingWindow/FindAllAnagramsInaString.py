import collections
from typing import List
class FindAllAnagramsInaString:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p, len_s = len(p), len(s)
        result = []
        if len_p > len_s:
            return result
        counter_p = collections.defaultdict(int)
        counter_s = collections.defaultdict(int)

        # initiate
        for i in range(len_p):
            counter_p[p[i]] = counter_p.get(p[i], 0) + 1
            if s[i] in p:
                counter_s[s[i]] = counter_s.get(s[i], 0) + 1
        if counter_s == counter_p:
            result.append(0)
        print(counter_s, counter_p)

        left, right = 0, len_p
        while right < len_s:
            l_char = s[left]
            if l_char in counter_p:
                counter_s[l_char] -= 1
                if counter_s[l_char] == 0:
                    del counter_s[l_char]
            left += 1

            r_char = s[right]
            if r_char in counter_p:
                counter_s[r_char] += 1
            right += 1
            if counter_s == counter_p:
                result.append(left)
        return result