class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-1*nums[i]
        heap=nums
        heapq.heapify(heap)

        count =0
        while count<k-1:
            heapq.heappop(heap)
            count=count+1

        return -heapq.heappop(heap)
        