class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res=""
        for s in strs:
            res=res+ str(len(s))+ ',' #append the sizes
        res=res+'#'
        for s in strs:
            res=res+ s
        return res

        


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes=[]
        result=[]
        i=0
        while s[i]!='#':
            cur=""
            while s[i]!=',':
                cur+=s[i]
                i+=1
            sizes.append(int(cur))
            i+=1
        i+=1
        for sz in sizes:
            result.append(s[i:i+sz])
            i+=sz
        return result