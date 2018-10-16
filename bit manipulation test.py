#counting 1 on binary representation
count=0
a=15
while a:
    a=a&(a-1)
    count+=1
print(count)

#add two integers
def getsum(a,b):
    return a if b==0 else getsum(a^b,(a&b)<<1)

print(getsum(15,4))
print(15&4)

#missing number
def missingnumber(nums):
    ret = 0
    for i in range(len(nums)):
        ret ^= i
        ret ^= nums[i]
    return ret ^len(nums)
print('missing number',missingnumber([0,2,3,4,5]))

#largest power of 2 and smaller or equal to the given number N
def largest_power(N):
    N=N|(N>>1)
    N = N | (N >> 2)
    N = N | (N >> 4)
    N = N | (N >> 8)
    N = N | (N >> 16)
    return (N+1)>>1
print(largest_power(3154))

#bitwise and of number range
def rangeBitwiseAnd(m, n):
    a = 0;
    while m != n:
        m >>= 1;
        n >>= 1;
        a+=1
    return m<<a
print(rangeBitwiseAnd(5,15))

#majority element
def majorityElement5(nums):
    bit = [0]*32
    for num in nums:
        for j in range(32):
            bit[j] += num >> j & 1
    res = 0
    for i, val in enumerate(bit):
        if val > len(nums)//2:
            # if the 31th bit is 1,
            # it means it's a negative number
            if i == 31:
                res = -((1<<31)-res)
            else:
                res |= 1 << i
    return res
print(majorityElement5([5,6,7,8,9,5,5,5,5]))

