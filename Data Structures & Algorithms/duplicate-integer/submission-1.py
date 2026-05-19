class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set() # O(1), hasmap que no almacena los elementos, pero funciona como un diccionario.
        for i in nums:
            if i in unique_numbers:
                return True
            unique_numbers.add(i)
        return False
        # Time Cost of operation = O(n)