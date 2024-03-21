class Solution(object):
    # def resolveNew(self,asteroids,new):
    #     if asteroids==[]:
    #         asteroids += [new]
    #         return
    #     if (asteroids[-1]<0 and new<0) or (asteroids[-1]>0 and new>0) or (asteroids[-1]<0 and new>0):
    #         asteroids += [new]
    #     elif abs(asteroids[-1])<abs(new):
    #         asteroids.pop()
    #         self.resolveNew(asteroids,new)
    #     elif abs(asteroids[-1])==abs(new):
    #         asteroids.pop()

    # def asteroidCollision(self, asteroids):
    #     res = asteroids[0:1]
    #     for i in range(1,len(asteroids),1):
    #         self.resolveNew(res,asteroids[i])
    #     return res

    def asteroidCollision(self, asteroids):
        res = []
        for ast in asteroids:
            while True:
                if res==[] or res[-1]<0 or ast>0:
                    res += [ast]
                    break
                elif res[-1]>-ast:
                    break
                elif res[-1]==-ast:
                    res.pop()
                    break
                else:
                    res.pop()

        return res