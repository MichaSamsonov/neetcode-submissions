class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            l = i + 1
            highest = 0
            while l < len(arr):
                if arr[l] > highest:
                    highest = arr[l]
                l += 1
            res.append(highest)
        
        res[-1] = -1
        return res
            