class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)# normal dictionary will show an error if the dict doesnt have an key and te programmer is accessing it 
        for s in strs:# s is every word
            sorteds= ''.join(sorted(s))#sorteds is an identifier
            res[sorteds].append(s)
        return list(res.values())        
        