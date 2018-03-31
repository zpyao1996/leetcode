class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordict=dict()
        for i in range(len(words)):
            self.wordict[words[i]]=self.wordict.get(words[i],[])+[i]


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1==word2:
            list1=self.wordict[word1]
            res=len(list1)
            for i in range(len(list1)-1):
                res=min(res,list1[i+1]-list1[i])

        else:
            list1 = self.wordict[word1]
            list2 = self.wordict[word2]
            return min([abs(i - j) for i in list1 for j in list2])