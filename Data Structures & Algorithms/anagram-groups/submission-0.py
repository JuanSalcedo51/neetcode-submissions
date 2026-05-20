class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_ids = {}
        for word in strs:
            character_count = [0]*26 # There are 26 characters from a to z, now count their frequency as a binary code.
            for character in word:
                character_index = ord(character) - ord('a') # ord works using ASCII code, in 'a' is 97
                character_count[character_index] += 1
            anagram_id = tuple(character_count)
            if anagram_id not in anagrams_ids:
                anagrams_ids[anagram_id] = [word]
            else:
                anagrams_ids[anagram_id].append(word)
        return list(anagrams_ids.values())