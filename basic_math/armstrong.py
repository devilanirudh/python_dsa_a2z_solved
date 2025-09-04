class Solution:
    def isArmstrong(self, n):
        length = len(str(n))
        a = length
        num_sum = 0
        while(a>0):
            sum = (n%10)**length
            print(sum)
            num_sum+=sum
            n=n//10
            a = a-1
        return num_sum

p1 = Solution()
print(p1.isArmstrong(153))