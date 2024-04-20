class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0 for _ in range(length)]
        hp = [[temperatures[0],0]]
        heapq.heapify(hp)
        for i in range(1,length):
            while hp and temperatures[i]>hp[0][0]:
                el=heapq.heappop(hp)
                res[el[1]]=i-el[1]
            heapq.heappush(hp,[temperatures[i],i])
        for e in hp:
            res[e[1]]=0
        return res
