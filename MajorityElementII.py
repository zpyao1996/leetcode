class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        if not nums:
            return ans
        firstcount = 0
        secondcount = 0
        for i in range(len(nums)):
            if firstcount == 0:
                firstcount += 2
                firstnum = nums[i]
                secondcount -= 1
            else:
                if firstnum == nums[i]:
                    firstcount += 2
                    secondcount -= 1
                else:
                    firstcount -= 1
                    if secondcount <= 0:
                        secondcount += 2
                        secondnum = nums[i]
                    else:
                        if secondnum == nums[i]:
                            secondcount += 2
                        else:
                            secondcount -= 1
            if firstcount < secondcount:
                firstcount, secondcount = secondcount, firstcount
                firstnum, secondnum = secondnum, firstnum
        counts1=0
        for i in range(len(nums)):
            counts1=counts1+1 if nums[i]==firstnum else counts1
        if counts1>len(nums)/3:
            ans.append(firstnum)
        if secondcount>0:
            counts2=0
            for i in range(len(nums)):
                counts2=counts2+1 if nums[i]==secondnum else counts2
            if counts2>len(nums)/3:
                ans.append(secondnum)

        return ans


sol=Solution()
a=[1,2,3,1,2]
print(sol.majorityElement(a))

