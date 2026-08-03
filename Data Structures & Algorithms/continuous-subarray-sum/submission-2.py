class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixsum=0
        table={0: -1} 
        for i,n in enumerate(nums):
            prefixsum+=n
            key=prefixsum%k
            if key in table:
                if i-table[key]>1:
                    return True
                continue
            
            table[key]=i
        return False

