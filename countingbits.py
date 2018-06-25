
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans=[0]
        length=1
        while length<num+1:
            list=[i+1 for i in ans]
            ans=ans+list
            length=length*2
        return ans[:num+1]
sol=Solution()
print(sol.countBits(2))