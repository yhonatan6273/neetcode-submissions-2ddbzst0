class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(i,j):
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
        l=0
        r=len(s)-1
        while l<=r:
            swap(l,r)
            l+=1
            r-=1
        