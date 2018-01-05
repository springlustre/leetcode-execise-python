def uniquePathsWithObstacles(obstacleGrid):

        v = []
        length = len(obstacleGrid[0])
        temp = -1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] ==0:
                v.append(1)
            else:
                temp = i
                break
        if temp>=0:
            v.extend([0 for _  in range(length-temp)])
        print(v)

        if len(obstacleGrid)==0:
            return 0
        if len(obstacleGrid[0])==1:
            for x in obstacleGrid:
                if x[0]==1:
                    return 0
            return 1

        for row in obstacleGrid[1:]:
            for i in range(0,len(row)-1):
                if row[i]==1 and row[i+1]==1:
                    v[i+1] = 0
                    v[i] = 0
                elif row[i]==1:
                    v[i] = 0
                elif row[i+1]==1:
                    v[i+1] = 0
                else:
                    v[i+1] = v[i+1]+v[i]

        return v[-1]


a = uniquePathsWithObstacles([[0,0],[0,1]])
print(a)
    
