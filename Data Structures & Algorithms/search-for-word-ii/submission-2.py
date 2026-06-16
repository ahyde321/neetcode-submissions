class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

class Solution:


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # create the trie tree
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        # convenience vars
        ROWS, COLS = len(board), len(board[0])
        
        # track result word (avoid duplicate word) and visited characters (avoid using a position multiple times)
        res, visit = set(), set()
        
        # coordinates, node we are at in the trie tree, the word so far
        def dfs(r, c, node, word):

            if (r < 0 or c < 0 or                                           # bounding
                r >= ROWS or c >= COLS or
                (r, c) in visit or board[r][c] not in node.children):       # used or exist in input list?
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            
            dfs(r + 1, c, node, word)                                       # recursive loop
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)

            

