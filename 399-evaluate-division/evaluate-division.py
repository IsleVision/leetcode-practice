class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}
        for i in range(len(values)):
            if equations[i][0] not in graph:
                graph[equations[i][0]]={}
            if equations[i][1] not in graph:
                graph[equations[i][1]]={}
            graph[equations[i][0]][equations[i][1]]=values[i]
            graph[equations[i][1]][equations[i][0]]=1.0/values[i]
        res=[]
        for qr in queries:
            visited=[qr[0]]
            paths = [[qr[0],1.0]]
            value = -1.0
            while paths:
                pt,vl = paths.pop(0)
                if pt not in graph:
                    continue
                for k,v in graph[pt].items():
                    if k==qr[1]:
                        value=vl*v
                        res +=[value]
                        paths=[]
                        break
                    if k not in visited:
                        paths += [[k,vl*v]]
                        visited+=[k]
            if value==-1.0:
                res+=[-1.0]
        return res
                        
