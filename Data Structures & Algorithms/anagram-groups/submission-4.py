class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        for idx in range(len(strs)):
            sorted_words[idx] = sorted(strs[idx])
        indices = [i for i in range(len(strs))]
        in_group = [] = []
        groups = []
        for idx1 in indices:
            if idx1 in in_group: 
                continue
            next_group = [strs[idx1]]
            for idx2 in indices: 
                if idx2 in in_group: 
                    continue
                elif (idx1 != idx2) & (sorted_words[idx1]==sorted_words[idx2]): 
                    next_group.append(strs[idx2])
                    in_group.append(idx2)
            in_group.append(idx1)
            groups.append(next_group)
        return groups
        





        