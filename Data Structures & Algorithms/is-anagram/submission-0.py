class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for c in s:
            map_s[c] = map_s.get(c, 0) + 1
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1
        if map_s == map_t:
            return True
        return False