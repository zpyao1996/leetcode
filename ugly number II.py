import heapq
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        numlist=[1,2,3,5]
        i=0
        while i < n:
            a=heapq.heappop(numlist)
            if a*2 not in numlist:
                heapq.heappush(numlist,a*2)
            if a * 3 not in numlist:
                heapq.heappush(numlist, a * 3)
            if a * 5 not in numlist:
                heapq.heappush(numlist, a * 5)
            i+=1
        return a
def nthUglyNumber(n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min((u2, u3, u5))
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]
sol=Solution()

print(nthUglyNumber(20))