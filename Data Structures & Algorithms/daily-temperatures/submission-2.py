class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                temp = stack.pop()
                res[temp[1]] = index - temp[1]
            
            stack.append((n,index))
                
        return res


