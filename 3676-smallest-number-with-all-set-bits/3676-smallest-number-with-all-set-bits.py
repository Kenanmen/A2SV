class Solution:
    def smallestNumber(self, n: int) -> int:
        x = n.bit_length()
        ans = 0
        for i in range(x):
            ans += (2**i)
        return ans

        