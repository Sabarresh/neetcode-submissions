class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        result = list()
        for index, num in enumerate(nums):
            complement  = target - num
            if complement in hashmap:
                result.append(hashmap[complement])
                result.append(index)
                return result
            else:
                hashmap[num] = index
        
        