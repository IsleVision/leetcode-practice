class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        length = len(costs)
        if length<=candidates*2:
            heapq.heapify(costs)
            return sum(heapq.nsmallest(k,costs))
        else:
            costs1=costs[:candidates]
            costs2=costs[length-candidates:]
            heapq.heapify(costs1)
            heapq.heapify(costs2)
            rm = costs[candidates:length-candidates]
            res = 0
            while k>0:
                print(res)

                if (costs1 and costs2 and costs1[0]<=costs2[0]) or not costs2:
                    res+=heapq.heappop(costs1)
                    if rm:
                        heapq.heappush(costs1,rm.pop(0))
                else:
                    res+=heapq.heappop(costs2)
                    if rm:
                        heapq.heappush(costs2,rm.pop())
                k-=1
            return res