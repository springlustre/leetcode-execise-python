def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        list1 = [[False for _ in range(9)] for _ in range(9)]
        list2 = [[False for _ in range(9)] for _ in range(9)]
        list3 = [[False for _ in range(9)] for _ in range(9)]
        for i in range(0,9):
                for j in range(0,9):
                        k = i//3*3 + j//3
                        x = board[i][j]
                        if x!='.':
                                t = int(x)-1
                                list1[i][t] = True
                                list2[j][t] = True
                                list3[k][t] = True
                                
        def dfs(board,list1,list2,list3):
                # print(board[0])
            # board[0][0] = str(2)
                for i in range(0,9):
                        for j in range(0,9):
                                if board[i][j]==u".":
                                        k = i//3*3+j//3
                                        for m in range(0,9):
                                                # print(list1[i][m],list2[j][m],list3[k][m])
                                                if not (list1[i][m] or list2[j][m] or list3[k][m]):
                                                        #行列九宫均不含该数字
                                                        list1[i][m] = True
                                                        list2[j][m] = True
                                                        list3[k][m] = True
                                                        board[i][j] = str(m+1)
                                                        # print(board[i][j])
                                                        if dfs(board,list1,list2,list3):
                                                                return True
                                                        
                                                        list1[i][m] = False
                                                        list2[j][m] = False
                                                        list3[k][m] = False
                                                        board[i][j] = u"."
                                        return False #均无法填充
                print(True)   
                return True #不存在空白
        # for i in range(8):
        #     print(board[i])
        dfs(board,list1,list2,list3)
        for i in range(8):
            print(board[i])

a = isValidSudoku([1,3,5,6])
print(a)
    
