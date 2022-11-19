length_list = [int(input()) for _ in range(9)]

def dfs(x):
    global find
    if len(q)==7:
        if sum(q)==100:
            q.sort()
            for _ in q:
                print(_)
                find = True
        return

    for i in range(x,9):
        q.append(length_list[i])
        dfs(i+1)
        q.pop()
        if find == True:
            break        
find =False
q=[]
dfs(0)
