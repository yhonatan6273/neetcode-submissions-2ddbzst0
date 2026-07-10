class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            cur_sum = target - nums[i]
            if cur_sum not in table:
                table[nums[i]] = i
            else:
                secend_idx = table[cur_sum]
                return [secend_idx,i]
