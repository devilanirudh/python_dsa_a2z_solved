class divisor1:
    def divisor(self,n):
        a = []
        for i in range(1,n):
            if (n%i==0):
                a.append(i)
            else:
                pass
        return a

p1 = divisor1()        
print(p1.divisor(20))
            