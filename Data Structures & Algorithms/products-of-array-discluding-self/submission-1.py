class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = [1] * len(nums)
        post = [1] * len(nums)

        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i]

        post[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums) -2, 0, -1):
            post[i] = post[i+1] * nums[i]

        for i in range(len(nums)):
            temp = 1
            if i != 0:
                temp = pre[i-1]
            if i != len(nums) -1:
                temp *= post[i+1]
            res.append(temp)

        return res
