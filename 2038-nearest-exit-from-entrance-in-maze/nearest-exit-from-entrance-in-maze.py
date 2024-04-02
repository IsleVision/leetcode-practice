from queue import Queue
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # m = len(maze)
        # n = len(maze[0])
        # max_int = 2**(m+n)
        # def bfs(position:List[int],visited:List[List[int]])->int:
        #     r=position[0]
        #     c=position[1]
        #     if r<0 or r>m-1 or c<0 or c>n-1 or maze[r][c]=='+':
        #         return max_int
        #     if r in (0,m-1) or c in (0,n-1):
        #         return len(visited) if len(visited)>0 else max_int
        #     lf,rt,up,dn = [max_int]*4
        #     if maze[r][c-1]=='.' and [r,c-1] not in visited:
        #         lf=bfs([r,c-1],visited+[[r,c]])
        #     if maze[r][c+1]=='.' and [r,c+1] not in visited:
        #         rt=bfs([r,c+1],visited+[[r,c]])
        #     if maze[r-1][c]=='.' and [r-1,c] not in visited:
        #         up=bfs([r-1,c],visited+[[r,c]])
        #     if maze[r+1][c]=='.' and [r+1,c] not in visited:
        #         dn=bfs([r+1,c],visited+[[r,c]])
        #     return min(lf,rt,up,dn)
        
        # r=entrance[0]
        # c=entrance[1]
        # if r in (0,m-1) or c in (0,n-1):
        #     st = min(bfs([r,c-1],[[r,c]]),bfs([r,c+1],[[r,c]]),bfs([r-1,c],[[r,c]]),bfs([r+1,c],[[r,c]]))
        #     return st if st!=max_int else -1

        # return bfs(entrance,[]) if bfs(entrance,[])!=max_int else -1

        # m = len(maze)
        # n = len(maze[0])
        # max_int = 2**(m+n)
        # visited =[]
        # def bfs(position:List[int], step:int)->int:
        #     nonlocal visited
        #     r=position[0]
        #     c=position[1]
        #     if r<0 or r>m-1 or c<0 or c>n-1 or maze[r][c]=='+':
        #         return max_int
        #     if r in (0,m-1) or c in (0,n-1):
        #         return step if step>0 else max_int
        #     visited += [[r,c]]
        #     print(visited)
        #     print(step)
        #     lf,rt,up,dn = [max_int]*4
        #     if maze[r][c-1]=='.' and [r,c-1] not in visited:
        #         lf=bfs([r,c-1],step+1)
        #     if maze[r][c+1]=='.' and [r,c+1] not in visited:
        #         rt=bfs([r,c+1],step+1)
        #     if maze[r-1][c]=='.' and [r-1,c] not in visited:
        #         up=bfs([r-1,c],step+1)
        #     if maze[r+1][c]=='.' and [r+1,c] not in visited:
        #         dn=bfs([r+1,c],step+1)
        #     return min(lf,rt,up,dn)
        
        # r=entrance[0]
        # c=entrance[1]
        # st = 0
        # if r in (0,m-1) or c in (0,n-1):
        #     visited=[[r,c]]
        #     st = min(bfs([r,c-1],1),bfs([r,c+1],1),bfs([r-1,c],1),bfs([r+1,c],1))
        #     return st if st!=max_int else -1
        
        # st = bfs(entrance,0)
        # return st if st!=max_int else -1
        # m = len(maze)
        # n = len(maze[0])
        # r0=entrance[0]
        # c0=entrance[1]
        # # visited = []
        # path = [[r0,c0,0]]
        # di = [[0,1],[1,0],[0,-1],[-1,0]]
        # s = -1
        # while path:
        #     r,c,s=path.pop(0)
        #     # visited +=[[r,c]]
        #     maze[r][c]='+'
        #     if (r!=r0 or c!=c0) and (r==0 or r==m-1 or c==0 or c==n-1):
        #         return s
        #     for d in di:
        #         r_n = r+d[0]
        #         c_n = c+d[1]
        #         if r_n>=0 and r_n<=m-1 and c_n>=0 and c_n<=n-1 and maze[r_n][c_n]=='.':
        #             path +=[[r_n,c_n,s+1]]
        #     # if r-1 >=0 and [r-1,c] not in visited and maze[r-1][c]=='.':
        #     #     path +=[[r-1,c,s+1]]
        #     # if c+1<=n-1 and [r,c+1] not in visited and maze[r][c+1]=='.':
        #     #     path +=[[r,c+1,s+1]]
        #     # if r+1<=m-1 and [r+1,c] not in visited and maze[r+1][c]=='.':
        #     #     path +=[[r+1,c,s+1]]
        #     # if c-1 >=0 and [r,c-1] not in visited and maze[r][c-1]=='.':
        #     #     path +=[[r,c-1,s+1]]
        # return -1
   
        q = Queue()
        q.put((entrance[0] , entrance[1] , 0))
        t = 0
        ans =[]
        maze[entrance[0]][entrance[1]] = "+"
 
        while(not q.empty()) :
            s = q.qsize()
            for i in range(s) :
                node = q.get() 
                # boundary conditions
                if node[0]==0 or node[0]==len(maze)-1 :
                    if node[2]!=0 :
                        return node[2]
                    ans += [node[2]]
                elif node[1] == 0 or node[1]==len(maze[0])-1 :
                    if node[2]!=0 :
                        return node[2]
                    ans += [node[2]]
                
                dx = [0 , -1 , 0 ,1 ]
                dy = [-1 , 0 , 1 , 0]

                for ind in range(4) :
                    x = node[0] + dx[ind]
                    y = node[1] + dy[ind] 
                    if x>=0 and x<len(maze) and y>=0 and y<len(maze[0]) and maze[x][y]!="+" :
                        maze[x][y] = "+"
                        q.put((x,y,node[2]+1))

        if len(ans) == 0:
            return -1 
    
        return -1 if max(ans)==0 else max(ans) 