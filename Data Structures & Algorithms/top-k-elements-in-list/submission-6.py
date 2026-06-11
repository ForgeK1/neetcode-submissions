class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #A base case to return all nums if # of nums present is the same as k
        if(k == len(nums)):
            return nums
        
        result = []
        hashmap = {}
        max_frequency = 0
        
        #Adds all numbers & their count as a key-value pair
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        #A for loop to get the max frequency of a number that shows up in the list
        for frequency in hashmap.values():
            if(max_frequency < frequency):
                max_frequency = frequency

            print(max_frequency)

        #A for loop to return k most frequent elements within the array
        while k > 0:
            # print(k)

            #Iterates through each num in the hashmap
            for num in hashmap.copy():
                #Checks which num matches the current max_frequency
                if(max_frequency == hashmap.get(num)):
                    result.append(num)
                    hashmap.pop(num)

                    break;
            
            #Decrements max_frequency & k for the next upcoming number
            if(max_frequency not in hashmap.values()):
                max_frequency -= 1
            
            k -= 1

        return result