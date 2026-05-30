from collections import deque
class Solution:
    

    def longestSubarray(self,nums: list[int], k: int) -> int:
        max_deque = deque()  # ישמור אינדקסים של ערכים בסדר יורד
        min_deque = deque()  # ישמור אינדקסים של ערכים בסדר עולה
        i = 0
        max_length = 0
        
        for j in range(len(nums)):
            # 1. עדכון תור המקסימום: נקה איברים קטנים יותר מ-nums[j]
            while max_deque and nums[max_deque[-1]] <= nums[j]:
                max_deque.pop()
            max_deque.append(j)
            
            # 2. עדכון תור המינימום: נקה איברים גדולים יותר מ-nums[j]
            while min_deque and nums[min_deque[-1]] >= nums[j]:
                min_deque.pop()
            min_deque.append(j)
            
            # 3. אם החלון לא תקין (|max - min| > k), צמצם משמאל
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                if max_deque[0] == i:
                    max_deque.popleft()
                if min_deque[0] == i:
                    min_deque.popleft()
                i += 1  # קידום האינדקס השמאלי
                
            # 4. עדכון האורך המקסימלי שנמצא
            max_length = max(max_length, j - i + 1)
            
        return max_length
            