class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):  # Loop through each row (0 to 8)
            r_count = set()  # Stores numbers seen in the current row
            c_count = set()  # Stores numbers seen in the current column
            for j in range(9):  # Loop through each column (0 to 8)
                # Validate row
                if board[i][j] != '.':  # Ignore empty cells
                    if board[i][j] in r_count:  # If duplicate found, return False
                        return False
                    r_count.add(board[i][j])  # Add number to set

                # Validate column
                if board[j][i] != '.':  # Ignore empty cells
                    if board[j][i] in c_count:  # If duplicate found, return False
                        return False
                    c_count.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_count = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i+k][j+l]
                        if num == '.':
                            continue
                        if num in box_count:
                            return False
                        box_count.add(num)
        
        return True
            