class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # solution1 not efficient enough
        # def checkOrders(ci:int, excld:Set[int], connections:List[List[int]])->int:
        #     cnt = 0
        #     for i in set(range(len(connections)))-excld:
        #         if ci in connections[i]: 
        #             excld.add(i)
        #             if connections[i][1]!=ci:
        #                 cnt +=1
        #                 cnt +=checkOrders(connections[i][1],excld,connections)
        #             else:
        #                 cnt +=checkOrders(connections[i][0],excld,connections)
        #     return cnt
        # return checkOrders(0,set(),connections)

        # nbrs ={ci:[] for ci in range(n)}
        # for con in connections:
        #     nbrs[con[0]]+=[con[1]]
        #     nbrs[con[1]]+=[con[0]]

        # visited = []
        # cities = [0]
        # chgs = 0
        # while cities:
        #     ci = cities.pop()
        #     for s_ci in nbrs[ci]:
        #         if s_ci in visited+cities:
        #             continue
        #         if [s_ci,ci] not in connections:
        #             chgs +=1
        #         cities+=[s_ci]
        #     visited+=[ci]
        # return chgs

        # nbrs ={ci:[] for ci in range(n)}
        # r_nbrs ={ci:[] for ci in range(n)}
        # for con in connections:
        #     nbrs[con[0]]+=[-con[1]]
        #     nbrs[con[1]]+=[con[0]]
        #     r_nbrs[con[0]]+=[con[1]]
        #     r_nbrs[con[1]]+=[con[0]]
        # visited=[]
        # cities=[0]
        # chg = 0
        # while cities:
        #     ci = cities.pop()
        #     for i in range(len(nbrs[ci])):
        #         if r_nbrs[ci][i] in visited+cities:
        #             continue
        #         if nbrs[ci][i] <0:
        #             chg +=1
        #         if r_nbrs[ci][i] not in visited+cities:
        #             cities+=[r_nbrs[ci][i]]
        #     visited +=[ci]
        # return chg

        # nbrs ={ci:[] for ci in range(n)}
        # for con in connections:
        #     nbrs[con[0]]+=[con[1]]
        #     nbrs[con[1]]+=[con[0]]  

        # visited = {0}
        # chg =0
        # def dfs(nd:int):
        #     nonlocal chg
        #     for nbr in nbrs[nd]:
        #         if nbr in visited:
        #             continue
        #         if [nbr,nd] not in connections:
        #             chg += 1
        #         visited.add(nd)
        #         dfs(nbr)
        # dfs(0)

        # return chg 
                    

        nbrs =[[] for _ in range(n)]

        for con in connections:
            nbrs[con[0]]+=[[con[1],-1]]
            nbrs[con[1]]+=[[con[0],1]]
        
        visited=[True]+[False]*(n-1)
        chg = 0
        def dfs(ci:int):
            nonlocal chg,visited
            for i in range(len(nbrs[ci])):
                if visited[nbrs[ci][i][0]]:
                    continue
                if nbrs[ci][i][1] ==-1:
                    chg +=1
                visited[nbrs[ci][i][0]]=True
                dfs(nbrs[ci][i][0])
        dfs(0)
        return chg

