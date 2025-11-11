class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
  
        length = len(strs)
        mem = {}
        def rec(idx,mc,nc):
            if idx>=length:
                return 0
            if (idx,mc,nc) not in mem:
                c0,c1 = strs[idx].count('0'),strs[idx].count('1')
                if c0 + mc <=m and c1+nc <=n:
                    mem[(idx,mc,nc)] = max(1+rec(idx+1,mc+c0,nc+c1),rec(idx+1,mc,nc))
                else:
                    mem[(idx,mc,nc)] = rec(idx+1,mc,nc)
            return mem[(idx,mc,nc)]
        return rec(0,0,0)




        
        
        