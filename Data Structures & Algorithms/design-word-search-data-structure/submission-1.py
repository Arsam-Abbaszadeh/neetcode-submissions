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
        def aux_search(suffix, startNode: ListNode, idx):
            curr = startNode
            for i, c in enumerate(suffix):
                if c == '.':
                    for child in curr.children.values():
                        if aux_search(suffix[i + 1:], child, idx + i):
                            return True
                    return False

                if c not in curr.children:
                    return False
                curr = curr.children[c]

            return curr.isWord
        return aux_search(word, self.root, 0)        