r,c,n = map(int, input().split())

stage = [list(input()) for _ in range(r)]

time = 0
bomb = []
bomb_time = set()
for i,s in enumerate(stage):
    for j in range(c):
        if s[j]=='O':
            bomb.append((i,j,time))
            bomb_time.add(time+3)
time += 1
while time<=n:
    if time==1:
        pass
    elif time==2:
        for i,s in enumerate(stage):
            for j in range(c):
                if s[j]=='.':
                    s[j] = 'O'
                    bomb.append((i,j,time))
                    bomb_time.add(time+3)
    else:
        if time in bomb_time:
            del_bomb = []
            for i,j,t in bomb:
                if time == t+3:
                    stage[i][j] = '.'
                    del_bomb.append((i,j))
                    if i+1<r:
                        stage[i+1][j] = '.'
                        del_bomb.append((i+1,j))
                    if i-1>=0:
                        stage[i-1][j] = '.'
                        del_bomb.append((i-1,j))
                    if j+1<c:
                        stage[i][j+1] = '.'
                        del_bomb.append((i,j+1))
                    if j-1>=0:
                        stage[i][j-1] = '.'
                        del_bomb.append((i,j-1))
            
            bomb_time.remove(time)

            for i,j,t in bomb:
                if (i,j) in del_bomb:
                    bomb.remove((i,j,t))
            
        if time%2==0:
            for i,s in enumerate(stage):
                for j in range(c):
                    if s[j]=='.':
                        s[j] = 'O'
                        bomb.append((i,j,time))
                        bomb_time.add(time+3)
    time += 1

for st in stage:
    for i,s in enumerate(st):
        if i<c-1:
            print(s,end='')
        else:
            print(s)
