class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        visits=set()
        res=[]
        if not nums:
            return res
        new_res=[]
        def dfs(i,nums,cur_target,new_res):
            nonlocal res
            

            if cur_target<0 or i>=len(nums):
                return
            if cur_target==0:
                if tuple(new_res) not in visits:
                    visits.add(tuple(new_res))
                    res.append(new_res.copy())
                return
                
            
            new_res.append(nums[i])
            dfs(i,nums,cur_target-nums[i],new_res)
            new_res.pop()
            dfs(i+1,nums,cur_target,new_res)





        
        
        dfs(0,nums,target,[])
        return res


        
        