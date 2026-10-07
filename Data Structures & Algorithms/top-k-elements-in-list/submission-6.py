class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ordered_nums = list()
        n = 0
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        hashmap_sorted = dict(sorted(hashmap.items(), key = lambda item:item[1], reverse=True))
        for num in hashmap_sorted.keys():
            if k > n:
                ordered_nums.append(num)
                n +=1
            else:
                break

        return ordered_nums
            