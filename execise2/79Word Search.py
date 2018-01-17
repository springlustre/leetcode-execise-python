def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    row = len(board)
    col = len(board[0])
    length = len(word)

    def search(board,r,c,word,i):
        if i==length:
            return True
        if r<0 or r>=row or c<0 or c>=col or board[r][c]!=word[i]:
            return False
        board[r][c] = "*"
        if search(board,r,c-1,word,i+1) or search(board,r,c+1,word,i+1) or search(board,r-1,c,word,i+1) or search(board,r+1,c,word,i+1):
            return True
        board[r][c] = word[i]


    for i in range(row):
        for j in range(col):
            if search(board,i,j,word,0):
                return True
    return False


a = exist([
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
],"ABCCED")

print(a)
    
