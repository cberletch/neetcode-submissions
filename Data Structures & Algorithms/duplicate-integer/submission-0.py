class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        orig_len = len(nums)

        s = set(nums)
        new_len = len(s)

        if orig_len == new_len:
            return False 
        
        return True