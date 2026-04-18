class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count the freq of each
        #appending 
        # sortit
        #last k
        hash_map={}
        for i in nums:            
            hash_map[i]=hash_map.get(i,0)+1
        arr=[]
        for num,cnt in hash_map.items():
            arr.append([cnt,num])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
        
        