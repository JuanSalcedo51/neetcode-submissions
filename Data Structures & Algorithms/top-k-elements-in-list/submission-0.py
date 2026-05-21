class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequencies = {}
        for num in nums:
            if num not in num_frequencies:
                num_frequencies[num] = 1
            else:
                num_frequencies[num] += 1

        num_buckets = len(nums)
        frequency_buckets = [[] for _ in range(num_buckets+ 1)]
        for num, frequency in num_frequencies.items():
            frequency_buckets[frequency].append(num)

        top_frequent_nums = []
        for index in range(len(frequency_buckets) - 1, -1, -1):
            for num in frequency_buckets[index]:
                top_frequent_nums.append(num)

                if len(top_frequent_nums) == k:
                    return top_frequent_nums

        # Time Complexity & Space Complexity O(n)