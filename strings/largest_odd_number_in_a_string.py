class Solution:
    def largestOddNumber(self, num: str) -> str:
        num1 = list(num.strip())
        occurence=-1
        for i in range(len(num1)):
            if (int(num1[i])%2==1):
                occurence = i+1

        if occurence>0:
            return num[:occurence]
        return num[:0]