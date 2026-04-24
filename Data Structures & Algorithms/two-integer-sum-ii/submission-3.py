class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            find = target - n
            if find > n:
                p = i + 1
                while p <= len(numbers)-1:
                    if find == numbers[p]:
                        return [i+1,p+1]
                    p += 1
            elif find < n:
                p = i -1
                while p >= 0:
                    if find == numbers[p]:
                        return [p+1,i+1]
                    p - 1

