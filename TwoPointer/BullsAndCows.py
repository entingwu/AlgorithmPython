import collections


class BullsAndCows:
    def getHint(self, secret: str, guess: str) -> str:
        A, B = 0, 0
        counter_s = collections.defaultdict(int)
        for char in secret:
            counter_s[char] = counter_s.get(char, 0) + 1
        print(counter_s)

        for i, char in enumerate(guess):
            char = guess[i]
            if char not in counter_s:
                continue
            if char == secret[i]:
                A += 1 # A
            else:
                B += 1 # B

            # adjust s=1122, g=1222
            if counter_s[char] < 1:
                B -= 1
            counter_s[char] -= 1

        return "{}A{}B".format(A, B)

