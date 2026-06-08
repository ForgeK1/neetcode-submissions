class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        '''
        Count the number of times a character appears in the array in a num : count
        key-value pair
        '''
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        #Iterate through each key and check if any number count goes beyond 1
        for num in hashmap:
            if(hashmap[num] > 1):
                return True
        
        #If no duplicates are found, then return False
        return False