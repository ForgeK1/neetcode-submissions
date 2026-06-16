class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Solution #2 (Neetcode) - Passed
        '''

        result = []
        bucket = [] #The length of this array is defined by the # of elements present in the nums array
        hashmap = {}
        
        '''
        Adds all numbers & their count as a key-value pair (counts the number of times 
        a number shows up)
        '''
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        #Fill each index of the bucket with an empty list
        for i in range(len(nums) + 1):
            bucket.append([])
        
        '''
        Iterates through each key of the hashmap, and adds the associated value
            Ex) HashMap = {"1" : 3, "2" : 1, "3" : 4}
        '''
        for num in hashmap:
            #Uses the # of frequences as the index for the bucket array
            bucket[hashmap.get(num)].append(num)
        
        index = len(bucket) - 1

        while(index >= 0 and k > 0):
            if(len(bucket[index]) != 0):
                for num in bucket[index]:
                    result.append(num)
                
                k -= 1

            index -= 1
        
        return result

        '''
        Solution #1 (My Solution) - Passed test cases but not submission
        '''
        
        # #A base case to return all nums if # of nums present is the same as k
        # if(k == len(nums)):
        #     return nums
        
        # result = []
        # hashmap = {}
        # max_frequency = 0
        
        # #Adds all numbers & their count as a key-value pair
        # for num in nums:
        #     hashmap[num] = 1 + hashmap.get(num, 0)
        
        # #A for loop to get the max frequency of a number that shows up in the list
        # for frequency in hashmap.values():
        #     if(max_frequency < frequency):
        #         max_frequency = frequency

        # #A for loop to return k most frequent elements within the array
        # while k > 0:
        #     #Iterates through each num in the hashmap
        #     for num in hashmap.copy():
        #         #Checks which num matches the current max_frequency
        #         if(max_frequency == hashmap.get(num)):
        #             result.append(num)
        #             hashmap.pop(num)

        #             break;
            
        #     #Decrements max_frequency & k for the next upcoming number
        #     if(max_frequency not in hashmap.values()):
        #         max_frequency -= 1
            
        #     k -= 1

        # return result