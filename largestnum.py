class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return None
        if len(nums)==1:
            return str(nums[0])
        ans=''
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                if self.compare(nums[j],nums[j-1]):
                    [nums[j],nums[j-1]]=[nums[j-1],nums[j]]
        ans=ans.join(nums)
        ans=str(int(ans))
        return ans



    def compare(self,a,b,i=0):
        if not i<len(a):
            return not self.cmpself(b,i,a[i-1])
        elif not i<len(b):
            return self.cmpself(a,i,b[i-1])
        if a[i]>b[i]:
            return True
        elif a[i]<b[i]:
            return False
        else:
            return self.compare(a,b,i+1)

    def cmpself(self,a,i,end):
        target=a[0]
        for j in range(i,len(a)):
            if a[j]>target:
                return True
            elif a[j]<target:
                return False
        return a[-1]>=end

nums=[121,12]
sol=Solution()

print(sol.compare('2281','2'))

