class Solution(object):
    def decodeString(self, s):
        num,nums = 0,''
        cont = ''
        cnt_l = 0
        cnt_r = 0
        res = ''
        for si in s:
            if cnt_l == cnt_r==0 and si.isalpha():
                res +=si
            elif cnt_l == cnt_r==0 and si.isdigit():
                nums+=si
            if cnt_l != cnt_r:
                cont += si

            if si=='[' and cnt_l==0:
                num = int(nums)
                nums = ''
                cnt_l +=1
            elif si =='[':
                cnt_l+=1
            elif si==']':
                cnt_r+=1
                if cnt_l==cnt_r==1:
                    cnt_l=cnt_r=0
                    res +=cont[0:-1]*num
                    cont=''
                elif cnt_l==cnt_r:
                    cnt_l=cnt_r=0
                    res +=self.decodeString(cont[0:-1])*num
                    cont=''            
        return res
