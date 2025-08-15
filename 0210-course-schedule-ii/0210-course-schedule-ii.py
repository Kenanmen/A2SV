class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        outdeg = [0] * numCourses
        for l,r in prerequisites:
            outdeg[l] +=1
            graph[r].append(l)
        q = deque([i for i in range(numCourses) if outdeg[i]==0])
        res = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                res.append(node)
                for ne in graph[node]:
                    outdeg[ne] -=1
                    if outdeg[ne] ==0:
                        q.append(ne)
        return res if len(res) == numCourses else []
        
        