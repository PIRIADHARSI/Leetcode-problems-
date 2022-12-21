class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        result= +2147483647
        nums.sort()
        for i in range(n-k+1):
            result=int(min(result,nums[i+k-1]-nums[i]))
        return result
