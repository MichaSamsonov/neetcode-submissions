class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while nums[i] < 1:
            num = nums[i]
            l, r = i + 1, len(nums) -1
            while l < r:
                if num + nums[l] + nums[r] == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                if num + nums[l] + nums[r] < 0:
                    l += 1
                if num + nums[l] + nums[r] > 0:
                    r -= 1
            if i == len(nums) -1:
                break
            while num == nums[i] and i < len(nums)-1:
                i += 1
        return res

            
