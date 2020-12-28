def solution(n, build_frame):
    answer = []
    mapp = [[0] * (n+1) for _ in range(n+1)]
    for frame in build_frame:
        print(mapp)
        print("iter...")
        x = frame[0]
        y = frame[1]
        if frame[2] == 0: # 1
            if frame[3] == 1: #install
                if frame[1] == 0 or mapp[y][x] & 1 == 1:
                    mapp[y][x] |= 1
                    #mapp[y+1][x] |= 1
            else: #remove
                if y < n + 1:
                    mapp[y][x] &= 2
                    
        else:#2
            if frame[3] == 1: #install
                if mapp[y][x] & 1 == 1:
                    mapp[y][x] |= 2
                elif x > 1 and x < n and mapp[y][x-1] & 2 == 2 and mapp[y][x+1] & 2 == 2:
                    mapp[y][x] |= 2
            else: # remove
                if x < n + 1:
                    mapp[y][x] &= 1
    for i in range(n+1):
        for j in range(n+1):
            if mapp[i][j] & 1 == 1:
                answer.append([j, i, 0])
            if mapp[i][j] & 2 == 2:
                answer.append([j, i, 1])
            
        
    return sorted(answer)


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
