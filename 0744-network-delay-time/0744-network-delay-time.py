class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        sub = defaultdict(list)
        for u, v, w in times:
            sub[u].append((w, v))
        heap =[]
        visited = set()
        heappush(heap,(0,k))
        t = 0
        
        while heap:
            wei,node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t, wei)
            for we,ne in sub[node]:
                if ne not in visited:
                    heappush(heap,(we+wei,ne))
     
        return t if len(visited) == n else -1