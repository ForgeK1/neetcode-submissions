'''
__Algorithm Explained__
1) Create an empty HashMap

2) Check if the difference of the target & value at each 
   index of the array exists in the current HashMap

3) If the value does not exist, add the current value to the 
   HashMap in a value : index pair

4) If the value exists, return the current array index and 
   the HashMap value index
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #Empty HashMap/dictionary
      hash_map = {}
      
      #Loops through each value of the nums array
      for i in range(len(nums)):
         #Finds the difference between the target & value
         difference = target - nums[i]

         '''
         Checks if the difference found exists in the HashMap, 
         
         If so, return the HashMap value index & array index
         '''
         if str(difference) in hash_map:
            return [hash_map.get(str(difference)), i]

         #Else, add the value : index pair to the HashMap
         else:
            hash_map[str(nums[i])] = i
