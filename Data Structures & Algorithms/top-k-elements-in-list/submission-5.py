class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_map = {}
        values = []
        for num in nums:
            value_map[num] = value_map.get(num, 0) + 1
        
        for value in value_map.values():
            values.append(value)
        
        values.sort(reverse=True)
        numList = {key for key, value in value_map.items() for i in range(k) if value == values[i]}

        return list(numList)
