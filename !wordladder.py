'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        w_dict={}
        wordList.append(beginWord)
        length = len(wordList)
        for i in range(length):
            for j in range(i+1,length):
                if self.connected(wordList[i],wordList[j]):
                    w_dict[wordList[i]]=w_dict.get(wordList[i],[])+[wordList[j]]
                    w_dict[wordList[j]] = w_dict.get(wordList[j],[]) + [wordList[i]]
        visited={}
        for i in wordList:
            visited[i]=False
        return self.bfs(beginWord, endWord, w_dict,visited)

    def connected(self,word1,word2):
        diff=0
        for i in range(len(word1)):
            if not(word1[i]==word2[i]):
                diff+=1
        if diff==1:
            return True
        return False

    def bfs(self,beginWord,endWord,w_dict,visited):
        aqueue=list();
        aqueue.append(beginWord)
        otherqueue = list();
        otherqueue.append(endWord)
        visited[beginWord]=visited[endWord]=True
        time=1
        while True:
            layer=list(aqueue)
            aqueue=[]
            if not layer:
                return 0
            time+=1
            while len(layer):
                a = layer.pop(0)
                if not w_dict.get(a):
                    continue
                for i in w_dict[a]:
                    if i in otherqueue:
                        return time
                    else:
                        if not visited[i]:
                            aqueue.append(i)
                            visited[i] = True
            aqueue,otherqueue=otherqueue,aqueue
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        if endWord not in wordList:
            return False
        visited={}
        for i in wordList:
            visited[i]=False
        return self.bfs(beginWord,endWord,wordList,visited)

    def bfs(self, beginWord, endWord, wordList, visited):
        aqueue=list();
        aqueue.append(beginWord)
        otherqueue = list();
        otherqueue.append(endWord)
        visited[beginWord]=visited[endWord]=True
        time=1
        while True:
            layer=list(aqueue)
            aqueue=[]
            if not layer:
                return 0
            time+=1
            while len(layer):
                a = layer.pop(0)
                for i in range(len(a)):
                    for j in range(ord('a'),ord('z')+1):
                        b=a[:i]+chr(j)+a[i+1:]
                        if b in otherqueue:
                            return time
                        if b in wordList and visited[b]==False:
                            visited[b]=True
                            wordList.remove(b)
                            aqueue.append(b)
            aqueue,otherqueue=otherqueue,aqueue
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]



sol=Solution()
print(sol.ladderLength(beginWord,endWord,wordList))

