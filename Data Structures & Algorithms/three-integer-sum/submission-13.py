class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # חובה למיון כדי להשתמש בשני מצביעים
        
        for i in range(len(nums) - 2):
            # דילוג על כפילויות עבור המספר הראשון (i)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    # רק אחרי שמצאנו פתרון, נדלג על כפילויות של j ו-k
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1  # הסכום קטן מדי, ננסה להגדיל אותו
                else:
                    k -= 1  # הסכום גדול מדי, ננסה להקטין אותו
        return res