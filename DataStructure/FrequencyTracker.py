import collections


class FrequencyTracker:

    def __init__(self):
        self.counter = collections.defaultdict(int)
        self.cnt_to_num = collections.defaultdict(set)

    def add(self, number: int) -> None:
        if number not in self.counter:
            self.counter[number] = 0
        freq = self.counter[number]
        self.counter[number] += 1

        if number in self.cnt_to_num[freq]:
            self.cnt_to_num[freq].remove(number)
        self.cnt_to_num[freq + 1].add(number)

    def deleteOne(self, number: int) -> None:
        if number not in self.counter:
            return None
        freq = self.counter[number]
        self.counter[number] -= 1
        if self.counter[number] == 0:
            del self.counter[number]

        if number in self.cnt_to_num[freq]:
            self.cnt_to_num[freq].remove(number)
        self.cnt_to_num[freq - 1].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.cnt_to_num:
            return len(self.cnt_to_num[frequency]) > 0
        return False

frequencyTracker = FrequencyTracker();
frequencyTracker.add(1)
frequencyTracker.deleteOne(1)
print(frequencyTracker.hasFrequency(1))
