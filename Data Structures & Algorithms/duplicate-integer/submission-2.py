class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set() # O(1), hasmap que no almacena los elementos, pero funciona como un diccionario.
        for num in nums:
            if num in unique_numbers:
                return True
            unique_numbers.add(num)
        return False
        # Time Cost of operation = O(n)