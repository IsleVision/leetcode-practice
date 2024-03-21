class RecentCounter(object):

    def __init__(self):
        self.counter = []        
    
    def ping(self, t):
        self.counter += [t]
        while self.counter[0]<t-3000:
                self.counter.pop(0)
        return len(self.counter)