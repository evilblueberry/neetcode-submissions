class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # [counter(act), set("act");
        
        dic = {}
        
        for word in strs:
            count = tuple(sorted(Counter(word).items()))
            if count in dic:
                dic[count].append(word)
            else:
                dic[count] = [word]

        result = []
        for item in dic:
            result.append(dic[item])

        return result