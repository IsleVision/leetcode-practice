class Solution:
    def dfs(self, adj: List[List[Tuple[int, int]]], visited: List[bool], minChange: List[int], currCity: int) -> None:
        visited[currCity] = True
        for neighbourCity in adj[currCity]:
            if not visited[neighbourCity[0]]:
                if neighbourCity[1] == 1:
                    minChange[0] += 1
                self.dfs(adj, visited, minChange, neighbourCity[0])
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], -1))
        visited = [False] * n
        minChange = [0]
        self.dfs(adj, visited, minChange, 0)
        return minChange[0]
        
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

        # def dfs(nd:int,visited:List[int], connections:List[List[int]])->int:
        #     chg = 0
        #     visited += [nd]
        #     for nbr in nbrs[nd]:
        #         if nbr in visited:
        #             continue
        #         if [nbr,nd] not in connections:
        #             chg += 1
        #         chg += dfs(nbr,visited,connections)
        #     return chg
        # return dfs(0,[],connections) 
                    

