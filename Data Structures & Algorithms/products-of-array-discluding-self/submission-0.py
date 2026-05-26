class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        reversed_nums = nums[::-1]
        preffix = []
        suffix = []

        accumulator_1 = 1
        for num in nums:
            preffix.append(accumulator_1)
            accumulator_1 = num * accumulator_1

        accumulator_2 = 1
        for num in reversed_nums:
            suffix.append(accumulator_2)
            accumulator_2 = num * accumulator_2

        suffix = suffix[::-1]

        product_nums = []
        for index in range(len(nums)):
            product_nums.append(preffix[index] * suffix[index])
        return product_nums
            