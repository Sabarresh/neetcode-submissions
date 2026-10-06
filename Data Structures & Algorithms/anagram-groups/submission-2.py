class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        result = []
        for word in strs:
            sw = sorted(word)
            sorted_word = ''.join(sw)
            
            if sorted_word in hashmap.keys():
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
            
        for _ in hashmap.values():
            result.append(_)
            
        return result
