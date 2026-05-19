class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_characters = {}
        t_characters = {}
        for character in s:
            if character not in s_characters:
                s_characters[character] = 1
            else:
                s_characters[character] += 1
        for character in t:
            if character not in t_characters:
                t_characters[character] = 1
            else:
                t_characters[character] += 1
        return s_characters == t_characters