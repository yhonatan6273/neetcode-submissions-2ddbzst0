class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        opt=[float("inf")]*(len(nums)+1)
        opt[0]=float("-inf")
        for n in nums:
            cur_ind=self.binarysearch(n,opt)
            if cur_ind==-1:
                continue
            else:
                opt[cur_ind]=n
        counter=0
        for i in range (1,len(opt)):
            if opt[i]!=float("inf"):
                counter+=1
               
            
        return counter

    def binarysearch(self,number,opt):
        l=0
        h=len(opt)-1
        res=-1
        while l<=h:
            mid=(l+h)//2
            if opt[mid]>=number:
                res=mid
                h=mid-1
            else:
                l=mid+1
        return res
        