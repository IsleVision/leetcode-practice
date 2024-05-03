class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length=len(gas)
        dif=[]
        idx=0
        for i in range(length):
            dif += [gas[i]-cost[i]]
            if dif[-1]>0:
                idx=i
        print(dif)
        if sum(dif)<0:
            return -1
        acc = dif[idx]
        acc_max = acc
        res = idx
        for i in range(idx-1,-1,-1):
            acc += dif[i]
            if acc>acc_max:
                res = i
                acc_max=acc
        return res
        