class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        amount_numbers = set() # O(1), hasmap que no almacena los elementos, pero funciona como un diccionario.
        for i in nums:
            if i in amount_numbers:
                return True
            amount_numbers.add(i)
        return False
        # Cost of operation = O(n)