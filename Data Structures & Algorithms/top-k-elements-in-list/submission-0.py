class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        for key in hashmap:
            if(hashmap[key] >= k):
                result.append(key)

        return result