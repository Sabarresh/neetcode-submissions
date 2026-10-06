class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        result = []
        for index, num in enumerate(nums):
            complement = target - num
            if complement in index_map.keys():
                result.append(index_map[complement])
                result.append(index)
            else:
                index_map[num] = index
        return result