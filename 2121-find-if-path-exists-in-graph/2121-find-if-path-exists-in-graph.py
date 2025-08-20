class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)
        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for ne in graph[node]:
                if ne not in visited:
                    found = dfs(ne)
                    if found:
                        return True
            return False
            
        return dfs(source)
        
        
       


                
            
            


        