class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            streak = 0
            while n in nums:
                n += 1
                streak += 1
            res = max(res,streak)
        return res