class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = dict()

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hsh:
                return sorted([hsh[pair], i])
            else:
                hsh[nums[i]] = i
                

            

            
    