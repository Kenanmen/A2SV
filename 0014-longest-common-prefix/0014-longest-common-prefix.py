class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comp = strs[0]
        for word in strs:
            temp = ''
            i = 0
            while i < len(comp) and i < len(word) and comp[i] == word[i]:
                temp += comp[i]
                i +=1
            comp = temp
            
        return comp  