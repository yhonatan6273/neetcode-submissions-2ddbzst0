class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]*(n+1)
        for i in range (n+1):
            cur_num_ones=self.count_one(i)
            res.append(cur_num_ones)
        return res
        



    def count_one(self,n):
        count=0
        while n!=0:
            cur_bit=1&n
            count+=cur_bit
            n>>=1
        return count