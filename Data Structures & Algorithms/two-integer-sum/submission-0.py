class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ma={}
        ind=0
        ans=[]
        for i in nums:

            check=target-i
            if check in ma:
                ans.append(ma[check])
                ans.append(ind)
            ma[i]=ind
            ind=ind+1
        
        return ans



        
        