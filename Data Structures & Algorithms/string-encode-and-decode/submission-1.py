class Solution:

    def encode(self, strs: List[str]) -> str:
        string_code = ""
        for string in strs:
            str_length = len(string)
            string_code += f"{str_length}#{string}"
        return string_code
    def decode(self, string_code: str) -> List[str]:
        index = 0
        original_str_list = []
        while index < len(string_code):
            auxiliar_index = index
            str_length = 0
            decoded_string = ""
            while string_code[auxiliar_index] != '#':
                auxiliar_index += 1
            else:
                str_length = int(string_code[index:auxiliar_index])
                decoded_string += string_code[auxiliar_index + 1 : auxiliar_index + str_length + 1]
                original_str_list.append(str(decoded_string))
                index = auxiliar_index + 1 + str_length
                str_length = 0
                decoded_string = ""
        return original_str_list

        # Time & Space Complexity = O(n+m)