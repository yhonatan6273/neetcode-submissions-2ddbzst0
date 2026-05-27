import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0

        # 1. ספירת תדירויות של המשימות (ייקח לכל היותר 26 מקום)
        counts = Counter(tasks)

        # 2. בניית ערימת מקסימום. בפייתון יש רק מינימום, אז נהפוך סימן למינוס
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        # 3. תור לניהול הצינון: ישמור זוגות של (תדירות נותרת, זמן שחרור)
        cooldown_queue = deque()

        time = 0

        # הלולאה רצה כל עוד יש משימות לבצע (או כאלו שזמינות או כאלו שבצינון)
        while max_heap or cooldown_queue:
            time += 1

            # א. שחרור משימות מהצינון אם הגיע זמנן
            if cooldown_queue and cooldown_queue[0][1] <= time:
                rem_count, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, rem_count)

            # ב. ביצוע המשימה הדחופה ביותר הזמינה כרגע
            if max_heap:
                # שולפים (זכור שהמספר שלילי, אז פלוס 1 בעצם מקרב אותו ל-0)
                current_task_count = heapq.heappop(max_heap) + 1

                # אם עדיין נשארו משימות מהסוג הזה, נשלח אותה לצינון
                if current_task_count < 0:
                    cooldown_queue.append((current_task_count, time + n+1))

            # ג. אם max_heap ריק, המשמעות היא שהשנייה הזו היא Idle.
            # הקוד פשוט ימשיך לשנייה הבאה מבלי לעשות כלום.

        return time