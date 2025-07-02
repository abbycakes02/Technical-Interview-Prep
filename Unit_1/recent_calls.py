class RecentCounter:

    def __init__(self):
        self.requests = []


    def ping(self, t: int) -> int:
        self.requests.append(t)
        answer = 0
        down_range = t-3000
        for i in self.requests:
            if down_range <= i <= t:
                answer+=1
        return answer


class Queue_RecentCounter:

    def __init__(self):
        self.requests = []


    def ping(self, t: int) -> int:
        self.requests.append(t)
        answer = 0
        down_range = t-3000
        for i in self.requests:
            if down_range <= i <= t:
                answer+=1
        return answer
    

class twopointer_RecentCounter:
    def __init__(self):
        # two pointer
        self.requests = []
        self.left = 0

    def ping(self, t: int) -> int:
        self.requests.append(t) # o(1)
        while self.requests[self.left] < t - 3000:
            self.left += 1
        return len(self.requests) - self.left
        # update range

class Circular_Buffer_RecentCounter:
    # wraps around
    def __init__(self):
        self.size = 1024
        self.buffer = [0] * 1000
        self.start = 0
        self.end = 0
    def ping(self, t: int) -> int:
        self.buffer[self.end & self.size] = t
        # fixed size buffer
        self.end+=1 
        while self.buffer[self.start] < t - 3000:
            self.start +=1
        return self.end - self.start
        # we add to buffer to the end
        
        # we move start pointer to wherever it's in the range
        # we return the end pointer - start pointer
    
class PeriodicCleanup_RecentCounter:
    # wraps around
    def __init__(self):
        self.requests = []
        self.compressinterval = 3000
        self.call_count = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.call_count += 1
        # periodic cleanup
        if self.call_count % self.compressinterval == 0:
            self.requests = [x for x in self.requests if x >=t - 3000]


        self.buffer[self.end & self.size] = t
        # fixed size buffer
        self.end+=1 
        while self.buffer[self.start] < t - 3000:
            self.start +=1
        return self.end - self.start