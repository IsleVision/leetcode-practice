class Solution(object):
    def isDivisor(self, str_ini, sub_str):
        return str_ini.replace(sub_str,'')==''
        
    def gcdOfStrings(self, str1, str2):
        i,j = 0,0
        length1 = len(str1)
        length2 = len(str2)
        gcd = ''
        gcd_tmp = ''

        while i < length1 and j < length2:
            if str1[i]==str2[j]:
                gcd_tmp += str1[i]
            else:
                break

            if length1%(i+1)==0 and length2%(i+1)==0 and self.isDivisor(str1,gcd_tmp) and self.isDivisor(str2,gcd_tmp):
                gcd = gcd_tmp   

            i+=1
            j+=1

        return gcd    
 







