class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Solution #2 (Neetcode) - Passed
        '''

        count = {}
        frequency = [[] for i in range(len(nums) + 1)] #The length of this array is defined by the # of elements present in the nums array (ex. 0 --> 7, includes 1 --> 6 indexes)
        result = []

        '''
        Adds all numbers & their count as a key-value pair (counts the number of times 
        a number shows up)
        '''
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        '''
        Iterates through each key of the count, and adds the associated value
            Ex) count = {"1" : 3, "2" : 1, "3" : 4}
        '''
        for n, c in count.items():
            #Uses count : num key value pair to append the num in the correct list
            frequency[c].append(n)
        
        '''
        Loop breakdown:
            - len(frequency) - 1: Indicates the last index of the list
            - 0: Indicates that the program iterates each index up until 0
            - -1: Indicates that the loop goes in decending order (ex. starting with the last index)
        '''
        for index in range(len(frequency) - 1, 0, -1):
            #A loop to iterate through each num in the inner list
            for num in frequency[index]:
                result.append(num)

            if(len(result) == k):
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