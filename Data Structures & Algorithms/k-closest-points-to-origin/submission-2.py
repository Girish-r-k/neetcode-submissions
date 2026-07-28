class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in range(len(points)):
            heap.append((points[i][0]**2+points[i][1]**2,[points[i][0],points[i][1]]))

        
        heapq.heapify(heap)
        ans=[]
        for i in range(k):
            dist,point=heapq.heappop(heap)
            ans.append(point)

        

        return ans