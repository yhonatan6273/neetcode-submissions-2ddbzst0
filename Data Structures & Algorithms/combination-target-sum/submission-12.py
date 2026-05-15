class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,cur_res,total):
            if (total==target):
                res.append(cur_res.copy())
                return
            if (i>=len(nums) or total>target):
                return
            cur_res.append(nums[i])
            dfs(i,cur_res,total+nums[i])
            cur_res.pop()
            dfs(i+1,cur_res,total)
        dfs(0,[],0)
        return res
