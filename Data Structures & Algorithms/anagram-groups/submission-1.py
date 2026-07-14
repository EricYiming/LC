class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)


        for str in strs: 
            count = [0] * 26
            for c in str: 
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            group[key].append(str)
        
        return list(group.values())

        
