class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {}
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            if word in anaMap:
                anaMap[word].append(strs[i])
            else:
                anaMap[word] = [strs[i]]  

        anagrams = []
        for anagram in anaMap.values():
            anagrams.append(anagram)

        return anagrams        