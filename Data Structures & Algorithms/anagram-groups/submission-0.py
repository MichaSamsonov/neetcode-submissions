class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        for wort in strs:
            sort = "".join(sorted(wort))
            sets.setdefault(sort, []).append(wort)
        
        output = []
        for value in sets.values():
            output.append(value)
        
        return output