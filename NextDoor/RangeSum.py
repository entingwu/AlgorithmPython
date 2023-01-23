# Given a list of numbers and a range (min/max; inclusive), find the sum of all the numbers in the list that are in this range.

# my_list = [3, 1, 5, 19, 20, 16]

# range [3, 5] should return 8
# range [2, 5] should return 8
# range [1, 5] should return 9

# what if the list is always the same? and we could get millions of different range calls on the same list

#                [1, 3 ,5, 16, 19, 20]
#              0  1  2  3  4   5   6
# prefix_sum   0  1  4  9  25  44  64
from typing import List

def prefix_sum(list) -> List[int]:
    prefix_sum = [0]
    for num in list:
        prefix_sum.append(prefix_sum[-1] + num)
    return prefix_sum

#   0  1  2   3   4   5
#  [1, 3 ,5, 16, 19, 20]
# find 2
def find_first_larger(arr, target) -> int:
    start, end = 0, len(arr) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid
        else:
            start = mid
    if arr[start] == target:
        return start
    return end

#   0  1  2  3   4   5
#  [1, 3, 5, 16, 19, 20]
#         s  e
# find 6
def find_last_less(arr, target) -> int:
    start, end = 0, len(arr) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid
        else:
            end = mid
    if arr[end] == target:
        return end
    return start

def preprocessing(my_list):
    sorted_list = sorted(my_list)
    presum = prefix_sum(sorted_list)
    return sorted_list, presum

def multi_range_sum(range) -> int:
    min, max = range
    left_idx = find_first_larger(sorted_list, min)
    right_idx = find_last_less(sorted_list, 6)
    range_sum = presum[right_idx + 1] - presum[left_idx]
    return range_sum

my_list = [3, 1, 5, 19, 20, 16]
sorted_list, presum = preprocessing(my_list)
print(multi_range_sum([1, 5]))

