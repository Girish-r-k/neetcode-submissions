class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        ma={}
        ans=[]
        heap=[]
        for i in nums:
            if not i in ma:
                ma[i]=1
            else:
                ma[i]+=1
        
        for n,freq in ma.items():
            heap.append((-freq,n))
        
        heapq.heapify(heap)
        for i in range(k):
            count,nu=heapq.heappop(heap)
            ans.append(nu)

        return ans

