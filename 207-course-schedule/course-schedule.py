class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        pathDic = {}
        for p in prerequisites:
            if p[0] not in pathDic:
                pathDic[p[0]]=[p[1]]
            else:
                pathDic[p[0]]+=[p[1]]
        notVis = pathDic.keys()-{prerequisites[0][0]}
        arr = [[prerequisites[0][0]]]
        while arr or notVis:
            if not arr:
                arr = [[notVis.pop()]]
            nd = arr[0][-1]
            if nd not in pathDic or not pathDic[nd]:
                arr.pop(0)
            else:
                ary = arr[0].copy()
                for i in range(len(pathDic[nd])):
                    nd_nx = pathDic[nd][i]
                    # print(arr,ary)
                    if nd_nx in ary:
                        return False
                    elif i==0:
                        arr[0]+=[nd_nx]
                    else:
                        arr += [ary+[nd_nx]]
                    notVis -= {nd_nx}
                del pathDic[nd]
        return True
