class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_to_list = defaultdict(list)

        for s in strs: 
            sorteds = "".join(sorted(s))
            master_to_list[sorteds].append(s)

        res = []
        for s, group in master_to_list.items(): 
            res.append(group)
        return res 


        