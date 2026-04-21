class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_map={}
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1

        for i in range(len(t)):
            if t[i] not in hash_map:
                return False
            else:
                hash_map[t[i]] = hash_map.get(t[i], 0) + 1

        return True

        