class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        length = len(searchWord)
        res=[[] for _ in range(length)]
        for i in range(length):
            wd = searchWord[0:i+1]
            cnt=0
            for pd in products:
                if pd.find(wd)==0:
                    res[i]+=[pd]
                    cnt+=1
            if i==0:
                res[i].sort()
                products=res[i]
            if cnt>3:
                res[i]=res[i][:3]
        return res

        