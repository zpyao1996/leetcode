class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(0)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for i in word:
            find=False
            for j in cur.next:
                if i==j.val:
                    cur=j
                    find=True
                    continue
            if not find:
                a=TreeNode(i)
                cur.next.append(a)
                cur=a
        cur.flag=True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in word:
            find=False
            for j in cur.next:
                if i==j.val:
                    find=True
                    cur=j
            if not find:
                return False
        if cur.flag:
            return True
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for i in prefix:
            find = False
            for j in cur.next:
                if i == j.val:
                    find = True
                    cur = j
            if not find:
                return False
        return True

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.flag=False
        self.next = []

atrie=Trie()
print(atrie.insert('abcd'))
print(atrie.search('abcd'))
print(atrie.search('456'))
print(atrie.startsWith('ab'))
