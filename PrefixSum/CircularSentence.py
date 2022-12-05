class CircularSentence:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        if len(words) == 0:
            return True
        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]
            print(word1, word2)
            print(word1[-1], word2[0])
            if word1[-1] != word2[0]:
                return False
        word1, word2 = words[0], words[-1]
        if word1[0] != word2[-1]:
            return False
        return True

