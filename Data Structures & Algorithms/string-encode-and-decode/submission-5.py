#Machine 1 ---encoded_string---> Machine 2 --> decoded_string
class Solution:
    def encode(self, strs: List[str]) -> str:      
        encoded_string = ""
        
        for string in strs:
            if(string == ""):
                string = "empty"

            if(encoded_string != ""):
                encoded_string = encoded_string + " " + string
            else:
                encoded_string = string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = s.split(" ")

        for i in range(len(decoded_string)):
            if(decoded_string[i] == "empty"):
                decoded_string[i] = ""
        
        return decoded_string