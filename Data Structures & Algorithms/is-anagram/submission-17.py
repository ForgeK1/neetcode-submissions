class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Solution #1: Arrays Big O(nlogn)
        '''

        '''
        
        #Checks if the lengths of both strings are the same
        if(len(s) != len(t)):
            return False
        
        s_list = []
        t_list = []

        #Adds each char of the s & t strings to their respective lists
        for i in range(len(s)):
            s_list.append(s[i])
            t_list.append(t[i])
        
        #Sorts the lists using the built in sort method
        s_list.sort()
        t_list.sort()

        #Loops through each character of both lists to see if all characters match
        for i in range(len(s_list)):
            if(s_list[i] != t_list[i]):
                return False
        
        #If all the characters match, then an anagram is detected
        return True

        '''

        '''
        Solution #2: HashMap Big O(nlogn)
        '''

        #Checks if the lengths of both strings are the same
        if(len(s) != len(t)):
            return False

        s_hashmap, t_hashmap = {}, {}

        '''
        Counts the number of time a character appears in a given strin and stores it in
        a HashMap through a character : count key-value pair
        '''
        for i in range(len(s)):
            s_hashmap[s[i]] = 1 + s_hashmap.get(s[i], 0) #Ex) "a": 1 + 1 + 1 --> 3 counted
            t_hashmap[t[i]] = 1 + t_hashmap.get(t[i], 0)

        #Compares the count of each character from both HashMaps
        for key in s_hashmap:
            if(s_hashmap.get(key) != t_hashmap.get(key, 0)):
                return False
        
        #If all character counts match, then an anagram is found
        return True