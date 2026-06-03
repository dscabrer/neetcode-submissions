class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        rep = False
        if len(num_set) < len(nums): 
            rep = True
        return rep
        