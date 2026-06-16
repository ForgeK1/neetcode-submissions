#Machine 1 ---encoded_string---> Machine 2 --> decoded_string
class Solution:
    def encode(self, strs: List[str]) -> str:      
        #Base case #1 (deals with empty lists)
        if(len(strs) == 0):
            return "-1"
        
        encoded_string = ""
        
        for string in strs:
            #Deals with empty strings
            if(string == ""):
                string = "empty"

            #And if-else statement to encode the list of strings into a string
            if(encoded_string != ""):
                encoded_string = encoded_string + "Z" + string
            else:
                encoded_string = string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        #Base case #1 (deals with empty lists)
        if(s is "-1"):
            return []
        
        #Uses a tokenizor to split the string into a list of strings
        decoded_string = s.split("Z")

        #If any "empty" strings are in the list, they are turned back into ""
        for i in range(len(decoded_string)):
            if(decoded_string[i] == "empty"):
                decoded_string[i] = ""
        
        return decoded_string