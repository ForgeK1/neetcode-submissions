#Machine 1 ---encoded_string---> Machine 2 --> decoded_string
class Solution:
    def encode(self, strs: List[str]) -> str:
        #Base case #1
        if(len(strs) == 1):
            return strs[0]
        
        encoded_string = ""
        
        for string in strs:
            # print(string)

            if(encoded_string != ""):
                encoded_string = encoded_string + " " + string
            else:
                encoded_string = string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        print(s)
        
        return s.split(" ")