class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        #Checks if the lengths of both strings are the same
        if(len(s) == len(t)):
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
        else:
            return False