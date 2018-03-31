class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign=False
        if (numerator<0 and denominator>0) or (numerator>0 and denominator<0):
            sign=True
            numerator=abs(numerator)
            denominator=abs(denominator)
        a=int(numerator/denominator)
        numerator=numerator % denominator
        numset=list()
        numset.append(numerator)
        b=[]
        while True:
            if numerator==0:
                break
            numerator*=10
            b.append(str(int(numerator/denominator)))

            numerator=numerator%denominator
            if numerator in numset:
                i=numset.index(numerator)
                b.insert(i,'(')
                b.append(')')
                break
            else:
                numset.append(numerator)
        if not b:
            ans=str(a)
        else:
            ans=str(a)+'.'+''.join(b)
        if sign:
            ans='-'+ans
        return ans

sol=Solution()

print(sol.fractionToDecimal(1,6))