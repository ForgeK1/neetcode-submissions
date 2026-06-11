class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        An empty HashMap to store our list of string anagram arrays
            #NOTE: defaultdict(list) means that it assigns a default 
                   value to all keys that have yet to be created, 
                   so in this case each key will start with an 
                   empty list
        '''
        result = defaultdict(list) 

        #A for loop to iterate through each string in the strs array
        for string in strs:
            '''
            Creates an array where each index maps to the position of the 
            alphabet a ... z, 0 ... 25
            '''
            count = [0] * 26

            #An inner for loop to iterate through each char in the curr string
            for char in string:
                char_index = ord(char) - ord('a') #ord gets the ASCII value of a character (Ex. ord(b) - ord(a) = 98 - 97 = 1)

                count[char_index] += 1

            '''
            We'll use the count array as a key to store our string. So if two strings have the
            same count array, then both strings will appear in the same array for the HashMap
            value
                NOTE: 
                    (1) count is converted to a tuple becaue a list cannot be used as a key
                    (2) append() is used since each default value for a key is an empty list
            '''
            result[tuple(count)].append(string)

            #Debug code
                #print(list(result.values()))

        #Since result.values() returns a dict_values object, it needs to be casted as a list
        return list(result.values())