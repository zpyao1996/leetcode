class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        w_dict = {}
        bank.insert(0,start)
        length = len(bank)
        for i in range(length):
            for j in range(i + 1, length):
                if self.connected(bank[i], bank[j]):
                    w_dict[bank[i]] = w_dict.get(bank[i], []) + [bank[j]]
                    w_dict[bank[j]] = w_dict.get(bank[j], []) + [bank[i]]
        visited = {}
        visited = {}
        for i in bank:
            visited[i] = False
        return self.bfs(start, end, w_dict, visited)

    def connected(self,word1,word2):
        diff=0
        for i in range(len(word1)):
            if not(word1[i]==word2[i]):
                diff+=1
        if diff==1:
            return True
        return False
    def bfs(self,beginWord,endWord,w_dict,visited):
        queue=list();
        queue.append(beginWord)
        visited[beginWord]=True
        time=1
        while len(queue):
            wordslayer=list(queue)
            queue=[]
            time+=1
            while len(wordslayer):
                a = wordslayer.pop(0)
                if not w_dict.get(a):
                    continue
                for i in w_dict[a]:
                    if i == endWord:
                        return time
                    else:
                        if not visited[i]:
                            queue.append(i)
                            visited[i] = True
        return 0