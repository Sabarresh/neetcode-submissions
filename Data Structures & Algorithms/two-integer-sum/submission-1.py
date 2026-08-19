class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        ans_list = []
        for index, num in enumerate(nums):
            complement = target - num
            if complement in index_map.keys():
                ans_list.append(index_map[complement])
                ans_list.append(index)
                return ans_list

            index_map[num] = index
