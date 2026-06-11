class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outerArr = [[]]

        return self.split(outerArr, strs, strs.pop(0))
    
    '''
    A method that compares the first string to every other string in the same list
        - If both strings are the same length & an anagram is found, keep in the same
          list
        
        - Else, put the string in a secondary list

        - Call the same method (recursion) to check the rest of the strings
    '''
    def split(self, outerArr, strs, starting_string):
        #Adds the starting string into the latest inner array
        outerArr[len(outerArr) - 1].append(starting_string)
        
        #Base case checks if the list of strings the program went through is empty
        if(len(strs) == 0):
            return outerArr
        #Second base case checks if there is one more string left in strs that has no corralation to any other strings
        if(len(strs) == 1):
            outerArr.append([strs.pop(0)])

            return outerArr
        
        tempArr = []

        #Compares each string in strs to the starting_string
        for i in range(len(strs)):
            #Checks if they're the same length
            if(len(starting_string) != len(strs[i])):
                tempArr.append(strs[i])
                continue
            
            #Checks if the strings result in an anagram
            if(self.is_anagram(starting_string, strs[i])):
                outerArr[len(outerArr) - 1].append(strs[i])
            else:
                tempArr.append(strs[i])

        '''
        If every string in strs is an anagram of the starting string,
        tempArr will be left empty. Therefore, the program can just return
        the outerArr
        '''
        if(len(tempArr) != 0):
            #Adds an empty array for the next batch of strings to be added to
            if(len(strs) > 1):
                outerArr.append([])

            return self.split(outerArr, tempArr, tempArr.pop(0))
        else:
            return outerArr
    
    #A method that checks if number of times a character appears for both strings are the same
    def is_anagram(self, str1, str2):
        hashmap_str1 = {}
        hashmap_str2 = {}

        for i in range(len(str1)):
            hashmap_str1[str1[i]] = 1 + hashmap_str1.get(str1[i], 0)
            hashmap_str2[str2[i]] = 1 + hashmap_str2.get(str2[i], 0)
        
        for char in hashmap_str1:
            if(hashmap_str1.get(char) != hashmap_str2.get(char, 0)):
                return False

        return True