from typing import (
    List,
)

class SortIntegers:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers(self, a: List[int]):
        if not a or len(a) == 0:
            return
        #self.quick_sort(a, 0, len(a) - 1)
        temp = [0 for i in range(len(a))]
        self.merge_sort(a, 0, len(a) - 1, temp)

    def merge_sort(self, a, start, end, temp):
        if start >= end:
            return
        mid = (start + end) // 2
        self.merge_sort(a, start, mid, temp)
        self.merge_sort(a, mid + 1, end, temp)
        self.merge(a, start, mid, end, temp)

    def merge(self, a, start, mid, end, temp):
        left, right = start, mid + 1
        index = start
        while left <= mid and right <= end:
            if a[left] < a[right]:
                temp[index] = a[left]
                left += 1
            else:
                temp[index] = a[right]
                right += 1
            index += 1

        while left <= mid:
            temp[index] = a[left]
            index += 1
            left += 1

        while right <= end:
            temp[index] = a[right]
            index += 1
            right += 1

        for i in range(start, end + 1):
            a[i] = temp[i]
            i += 1



    def quick_sort(self, a, start, end):
        if start >= end:
            return
        # 1. pivot, a[start], a[end]
        # get value not index
        pivot = a[(start + end) // 2]
        left, right = start, end

        # 2. left <= right not left < right
        while left <= right:
            # 3. a[left] < pivot not <=
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1

        self.quick_sort(a, start, right)
        self.quick_sort(a, left, end)

