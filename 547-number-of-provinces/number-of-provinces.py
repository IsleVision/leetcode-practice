class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def findCon( isConnected: List[List[int]], cons:Set[int], ci:int):
            for i in range(len(isConnected[ci])):
                if isConnected[ci][i]==1 and i not in cons:
                    cons.add(i)
                    cons |= findCon(isConnected,cons,i)
            return cons

        cities = set(range(len(isConnected)))
        group_num =0
        while cities:
            city = cities.pop()
            cons = findCon(isConnected,{city},city)
            if cons:
                group_num +=1
                cities -=cons
        return group_num