from typing import List
class MaximumProductSubarray:

    def maxProduct(self, nums: List[int]) -> int:
        max_product, n = float('-inf'), len(nums)
        fmax = [0] * n
        fmin = [0] * n

        fmax[0] = fmin[0] = nums[0]
        for i in range(1, n):
            fmax[i] = fmin[i] = nums[i]
            if nums[i] > 0:
                fmax[i] = max(nums[i] * fmax[i - 1], fmax[i])
                fmin[i] = min(nums[i] * fmin[i - 1], fmin[i])
            else:
                fmax[i] = max(nums[i] * fmin[i - 1], fmax[i])
                fmin[i] = min(nums[i] * fmax[i - 1], fmin[i])
            max_product = max(fmax[i], max_product)
        print(fmax)
        print(fmin)
        return max_product

    # TLE: Time: O(N^2)
    def maxProduct1(self, nums: List[int]) -> int:
        max_product, n = float('-inf'), len(nums)
        for i in range(n):
            product = 1
            for j in range(i, n):
                product = nums[j] * product
                max_product = max(product, max_product)
        return max_product