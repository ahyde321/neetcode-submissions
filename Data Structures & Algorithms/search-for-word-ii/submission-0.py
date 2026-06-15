class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, prefix):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            prefix += board[r][c]
            if node.word:
                res.add(prefix)
            
            dfs(r + 1, c, node, prefix)
            dfs(r - 1, c, node, prefix)
            dfs(r, c + 1, node, prefix)
            dfs(r, c - 1, node, prefix)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)