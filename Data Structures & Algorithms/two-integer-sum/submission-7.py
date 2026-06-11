class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        #Sorts the array before comparison
        nums.sort()

        while(i <= j):
            posResult = nums[i] + nums[j]
            posTarget = target

            #Converts result and target to positive integers before comparison
            if(posResult < 0 and posTarget < 0):
                posResult = posResult * -1
                posTarget = posTarget * -1

            print(posResult)
            print(str(posTarget) + '\n')
            print(i)
            print(str(j) + '\n')

            if(posResult == posTarget):
                return [i, j]             

            elif(posResult < posTarget):
                i += 1

            elif(posResult > posTarget):
                j -= 1

        return []