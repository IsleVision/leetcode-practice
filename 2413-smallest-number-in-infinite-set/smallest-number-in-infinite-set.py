class SmallestInfiniteSet:

    def __init__(self):
        self.vac = set()

    def popSmallest(self) -> int:
        if not self.vac:
            self.vac.add(1)
            return 1
        else:
            for i in range(1,len(self.vac)+1):
                if i not in self.vac:
                    self.vac.add(i)
                    return i
            self.vac.add(len(self.vac)+1)
            return len(self.vac)

    def addBack(self, num: int) -> None:
        if num in self.vac:
            self.vac.remove(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)