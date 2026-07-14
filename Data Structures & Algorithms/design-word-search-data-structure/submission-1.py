class TrieNode: 

    def __init__(self): 
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True        

    def search(self, word: str) -> bool:

        def dfs(i, parent): 
            if i == len(word) - 1:
                if word[i] == ".": 
                    for child in parent.children.values(): 
                        if child.endWord: 
                            return True
                return word[i] in parent.children and parent.children[word[i]].endWord
            
            if word[i] == ".": 
                for possible in parent.children: 
                    if dfs(i + 1, parent.children[possible]): 
                        return True
                return False
            else: 
                if word[i] not in parent.children: 
                    return False
                else: 
                    return dfs(i + 1, parent.children[word[i]])
        
        return dfs(0, self.root)
                
        
