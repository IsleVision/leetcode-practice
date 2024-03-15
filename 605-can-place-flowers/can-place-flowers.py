class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        cont_0 = -1
        plot_cnt = 0
        length_flowerbed= len(flowerbed)
        for i in range(length_flowerbed):
            if flowerbed[i]==1:
                cont_0 =-2
            if flowerbed[i]==0:
                cont_0 +=1
            if i == length_flowerbed-1 and cont_0==0:
                plot_cnt += 1

            if cont_0 ==1 :
                plot_cnt +=1
                cont_0 =-1    

        return plot_cnt>=n
            


        