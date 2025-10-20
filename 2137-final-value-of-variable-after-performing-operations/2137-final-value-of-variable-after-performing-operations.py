class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        x = 0
        for i in range(len(op)):
            if '--' in op[i]:
                x -=1
            else:
                x +=1
        return x
        