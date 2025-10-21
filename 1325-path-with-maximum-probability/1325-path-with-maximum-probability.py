class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], suc: List[float], start: int, en: int) -> float:
        graph = defaultdict(list)
        for idx,(l, r) in enumerate(edges):
            graph[l].append((r,suc[idx]))
            graph[r].append((l,suc[idx]))
        dicts = defaultdict(lambda : float("-inf"))

        dicts[start] = 0
        heap = [(-1, start)]
        visited = set()
        while heap:
            dist,node = heappop(heap)
            dist *= -1
            if node in visited:
                continue
            visited.add(node)
            for ne,we in graph[node]:
                update = we*dist
                if update > dicts[ne]:
                    dicts[ne] = update
                    heappush(heap,(-1 *update,ne))
        return dicts[en] if dicts[en] != float('-inf') else 0




        