class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count=0
        re=[-1,-1]
        res=float("infinity")
        l=0
        freq={}
        window={}
        for i in range(len(t)):
            freq[t[i]]=1+freq.get(t[i],0) 
        have,need=0,len(freq)
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if s[r] in freq and window[s[r]]==freq[s[r]]:
                have+=1
            while have==need:
                res=min(res,r-l+1)
                re=[l,r]
                window[s[l]]-=1
                if s[l] in freq and window[s[l]]<freq[s[l]]:
                    have-=1
                l+=1
        l,r=re
        return s[l:r+1]


            



               