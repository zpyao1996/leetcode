import string

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if endWord not in wordList:
            return 0
        return self.bfs(beginWord, endWord, wordset)

    def bfs(self, beginWord, endWord, wordset):
        aqueue = set([beginWord])
        otherqueue = set([endWord]);
        #visited[beginWord]=visited[endWord]=True
        time=1
        while True:
            tem_queue = set()
            if not aqueue:
                return 0
            time+=1
            for a in aqueue:
                for i in range(len(a)):
                    for j in string.ascii_lowercase:
                        b = a[:i]+j+a[i+1:]
                        if b in otherqueue:
                            return time
                        if b in wordset:
                            wordset.remove(b)
                            tem_queue.add(b)
            aqueue, otherqueue = otherqueue, tem_queue

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]

sol=Solution()
print(sol.ladderLength(beginWord,endWord,wordList))

