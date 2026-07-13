class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
       #1231
        div=1
        while x>=10*div:
            div*=10
        while x>0:
            #1
            first=x//div
            #1
            last=x%10
            if first!=last:
                return False
            x=(x%div)//10
            div=div//100
        return True

        


        