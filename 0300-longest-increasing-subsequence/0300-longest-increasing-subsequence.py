class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [0] *len(nums)
        for k in range(len(nums)):
            mem[k] = 1
            for i in range(k):
                if nums[i] < nums[k]:
                    mem[k] = max(mem[k],mem[i]+ 1)
        return max(mem)


        