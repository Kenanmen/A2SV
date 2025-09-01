class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        heap = []
        for p, v in classes:
            gain = -1 *((p+1)/(v+1) - (p/v))
            heapq.heappush(heap, (gain,p, v))
        for i in range(extraStudents):
            gain,p, v = heapq.heappop(heap)
            p, v = p+1,v+1
            gain = -1 *((p+1)/(v+1) - (p/v))
            heapq.heappush(heap, (gain,p,v))
        tot = 0
        for i, p,v in heap:
            tot += (p/v)
        return tot/len(classes)
            
        