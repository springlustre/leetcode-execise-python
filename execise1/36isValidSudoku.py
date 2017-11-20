def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        list1 = [[] for _ in range(9)]
        list2 = [[] for _ in range(9)]
        list3 = [[] for _ in range(9)]
        for i in range(9):
                for j in range(9):
                        x = board[i][j]
                        if x!='.':
                                #print(i//3*3+j//3)
                                if x in list1[i] or x in list2[j] or x in list3[i//3*3+j//3]:
                                        return False
                                else:
                                        list1[i].append(x)
                                        list2[j].append(x)
                                        list3[i//3*3+j//3].append(x)
        return True

a = isValidSudoku([1,3,5,6])
print(a)
    
