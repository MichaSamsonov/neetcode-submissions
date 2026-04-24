class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        num_map = {}
        for i in nums:
            find = target - i 
            if find in num_map:
                return [num_map[find], index]
            num_map[i] = index 
            index+=1
        
        
        