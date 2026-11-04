class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = dict()
        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1
        
        numsCount_sorted = dict(sorted(numsCount.items(), key = lambda item: item[1], reverse = True))
        keyList = list(numsCount_sorted)
        result = keyList[:k]

        return result