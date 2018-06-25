class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        cmax=0
        strlist=input.split('\n')
        clist=[]
        for i in strlist:
            j=1
            while i.startswith('\t'*j):
                j+=1
            j-=1
            clist=clist[:j]
            clist.append(i[j:])
            if '.' in i:
                clength=sum(map(len,clist))+j
                cmax=max(cmax,clength)
        return cmax
# better solution
def lengthLongestPath( input):
    maxlen = 0
    pathlen = {0: 0}
    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxlen

inpus='a.txt'
inputstr="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
sol=Solution()
print(sol.lengthLongestPath(inpus))