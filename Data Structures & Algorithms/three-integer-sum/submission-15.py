class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = []
    
        for i in range(len(nums)):
            # מניעת כפילויות עבור המצביע הראשון i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # אתחול המצביעים - בתוך הלולאה!
            l = i + 1
            h = len(nums) - 1
            
            while l < h:
                cur_sum = nums[i] + nums[l] + nums[h]
                
                if cur_sum == 0:
                    res.append([nums[i], nums[l], nums[h]])
                    
                    # קידום המצביעים ומניעת כפילויות עבור l ו-h
                    l += 1
                    h -= 1
                    while l < h and nums[l] == nums[l - 1]:
                        l += 1
                    while l < h and nums[h] == nums[h + 1]:
                        h -= 1
                        
                elif cur_sum < 0:
                    l += 1
                else:
                    h -= 1
                    
        return res
        