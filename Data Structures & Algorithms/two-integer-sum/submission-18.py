class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Create an empty HashMap/Dictionary to store the values & their associated indexes 
        after the program for every number checked from nums
        ''' 
        hash_map = {}

        #An index tracker to help the hash_map store the indexes associated with each value 
        curr_index = 0

        #A for loop to iterate through each value of nums
        for num in nums:
            #Gets the difference between the target & the curr number
            num_to_find = target - num

            '''
            If the difference found exists in the hash_map, the program returns the indexes
            of both values
            '''
            if(str(num_to_find) in hash_map):  
                #Debug code
                    #print('[' + str(hash_map.get(str(num_to_find))) + ', ' + str(curr_index) + ']')

                return [hash_map.get(str(num_to_find)), curr_index]
            #Else, the value & associated index is stored in the hash_map for a future num_to_find to check against
            else:
                hash_map[str(num)] = curr_index

            #The index tracker is incremented to keep up with the index of each number in the nums list
            curr_index += 1
        
        return None