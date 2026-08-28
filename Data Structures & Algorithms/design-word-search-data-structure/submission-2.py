class WordDictionary:
    def __init__(self):
        self.trie = Trie()        

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)
        
class ListNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = ListNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = ListNode()
            curr = curr.children[c]
        curr.isWord = True
    
    def search(self, word) -> bool:
        def aux_search(j, startNode: ListNode):
            curr = startNode
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if aux_search(i + 1, child):
                            return True
                    return False

                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]

            return curr.isWord
        return aux_search(0, self.root)        