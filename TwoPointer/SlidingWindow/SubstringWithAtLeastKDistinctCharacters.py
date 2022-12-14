from collections import defaultdict


class SubstringWithAtLeastKDistinctCharacters:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def k_distinct_characters(self, s: str, k: int) -> int:
        if not s or len(s) == 0:
            return 0

        n, substr_count = len(s), 0
        counter = defaultdict(int)
        distinct_chars = 0
        j = 0

        for i in range(n):
            while j < n and distinct_chars < k:
                char = s[j]
                counter[char] += 1
                if counter[char] == 1:
                    distinct_chars += 1
                j += 1

            if distinct_chars >= k:
                substr_count += n - j + 1

            pre_char = s[i]
            counter[pre_char] -= 1
            if counter[pre_char] == 0:
                distinct_chars -= 1

        return substr_count

