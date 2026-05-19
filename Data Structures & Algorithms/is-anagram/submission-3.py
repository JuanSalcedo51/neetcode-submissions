class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_characters = {}
        t_characters = {}
        for character in s:
            s_characters[character] = s_characters.get(character, 0) + 1
        for character in t:
            t_characters[character] = t_characters.get(character, 0) + 1
        return s_characters == t_characters