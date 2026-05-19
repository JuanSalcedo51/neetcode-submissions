class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        analyzed_num = {}
        index = 0
        for num in nums:
            difference = target - num
            if difference in analyzed_num:
                return [analyzed_num[difference], index]
            analyzed_num[num] = index
            index += 1