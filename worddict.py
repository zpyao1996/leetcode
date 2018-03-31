class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.worddict=set()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.worddict.add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if '.' not in word:
            return word in self.worddict
        else:
            position=[]
            for i in range(len(word)):
                if word[i]=='.':
                    position.append(i)
            alist=[[i for i in j] for j in self.worddict if len(j)==len(word)]
            for i in range(len(alist)):
                for j in position:
                    alist[i][j]='.'
                alist[i]=''.join(alist[i])
            return word in alist