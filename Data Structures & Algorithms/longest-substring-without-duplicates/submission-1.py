class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=[]
        res=0
        l=0
        r=0
        while r<len(s):
            while s[r]in window:
                window.remove(s[l])
                l+=1
            window.append(s[r])
            res=max(res,r-l+1)
            r+=1
        return res



        