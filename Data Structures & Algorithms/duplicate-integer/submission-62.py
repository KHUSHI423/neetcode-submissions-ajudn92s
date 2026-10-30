class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq=set()
        for i in nums:
            if i in freq:
                return True
            freq.add(i)
        return False
        

        '''index=0
        for i in nums:
            index=i ^ index
        if index:
            return True
        return False'''
        '''freq={}
        for i in nums:
            if i in freq:
                return True
            freq[i]=1+freq.get(i,0)
        return False'''        