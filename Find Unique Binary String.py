lass Solution(object):
    def findDifferentBinaryString(self, nums):
        l=len(nums[0]) 
        if nums[0]=="1": 
            return "0"
        for i in range(0,2**(l)): 
            b=bin(i)[2:].zfill(l) 
            if b not in nums: 
                return b
        
