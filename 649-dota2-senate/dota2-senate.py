class Solution(object):
    def predictPartyVictory(self, senate):
        cnt = 0
        se_a = list(senate)
        while len(se_a)!=abs(cnt):
            se_a_head = se_a[0]

            if cnt >0 and se_a[0]=='D':
                se_a.pop(0)
            elif cnt<0 and se_a[0]=='R':
                se_a.pop(0)
            else:
                tmp= se_a.pop(0)
                se_a += [tmp]
                
            if se_a_head=='R':
                cnt+=1
            else:
                cnt-=1
        return 'Dire' if se_a[0]=='D' else 'Radiant'

