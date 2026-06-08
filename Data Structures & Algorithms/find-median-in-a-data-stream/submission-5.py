class MedianFinder:

    def __init__(self):
        # declare small (max heap) and large (min heap)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # check values if values in small are greater than in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        # check size of small and large are within 1 of each other
        if len(self.small) > (len(self.large) + 1):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        if len(self.large) > (len(self.small) + 1):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (((self.small)[0] * -1) + self.large[0]) / 2
        
        