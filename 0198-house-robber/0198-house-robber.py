class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1]*len(nums)
        def rec(i):
            if i == 0:
                mem[0] == nums[0]
                return nums[0]
            elif i == 1:
                
                return max(nums[0],nums[1])
            else:
                if mem[i] != -1:
                    return mem[i]
                val = max(nums[i]+rec(i-2),rec(i-1))
                mem[i] = val
                return val
        return rec(len(nums)-1)
            

