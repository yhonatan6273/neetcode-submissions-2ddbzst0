class MinStack:

    def __init__(self):
        # מחסנית יחידה שתחזיק טאפלים של (value, current_min)
        self.stack = []

    def push(self, val: int) -> None:
        # אם המחסנית ריקה, הערך הנוכחי הוא גם המינימום של עצמו
        if not self.stack:
            self.stack.append((val, val))
        else:
            # אם היא לא ריקה, נראה מה המינימום שהיה עד עכשיו
            # המינימום שמור באינדקס 1 של הטאפל שנמצא בראש המחסנית
            current_min = self.stack[-1][1]
            # נדחוף את הערך החדש יחד עם המינימום המעודכן
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        # פשוט מוציאים את הטאפל האחרון. המינימום הישן נחשף אוטומטית מתחתיו
        self.stack.pop()

    def top(self) -> int:
        # מחזירים את הערך (אינדקס 0) מראש המחסנית
        return self.stack[-1][0]

    def getMin(self) -> int:
        # מחזירים את המינימום (אינדקס 1) מראש המחסנית
        return self.stack[-1][1]