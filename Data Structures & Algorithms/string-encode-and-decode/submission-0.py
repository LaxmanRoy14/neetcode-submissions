class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # Append the length of the string, a '#', and the string itself
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded_strs = []
        i = 0
        
        while i < len(s):
            # Find the index of the next '#' to extract the length
            j = i
            while s[j] != '#':
                j += 1
            
            # The length is the integer between i and j
            length = int(s[i:j])
            
            # The actual string starts after the '#' and ends 'length' characters later
            start_of_string = j + 1
            end_of_string = start_of_string + length
            
            decoded_strs.append(s[start_of_string : end_of_string])
            
            # Move the pointer to the start of the next encoded string chunk
            i = end_of_string
            
        return decoded_strs