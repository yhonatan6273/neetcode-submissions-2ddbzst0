class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        
        for i in range (len(nums)):
            cur_key=target-nums[i]
            if cur_key in hash_map:
                res=[hash_map[cur_key],i]
            else:
                hash_map[nums[i]]=i
        return res

                

        