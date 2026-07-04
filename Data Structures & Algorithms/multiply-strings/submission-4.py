class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit1 = ord(num1[i1]) - ord('0')
                digit2 = ord(num2[i2]) - ord('0')
                digit = digit1 * digit2
                pos=i1 + i2
                total=res[pos]+digit
                res[pos] =total%10
                res[pos + 1] += total//10
               

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        
        return "".join(map(str,res[beg:]))

    