class MedianFinder:

    def __init__(self):
        self.arr = [] 

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        # now we want to bubble down
        i = len(self.arr) - 1
        while i > 1 and self.arr[i - 1] > num:
            self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
            i -= 1
        print(f"Adding number {num}")
        print(self.arr)

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 1:
            # if odd
            return self.arr[len(self.arr) // 2]
        else:
            # if even 
            return (self.arr[len(self.arr) // 2 - 1] + self.arr[len(self.arr) // 2]) / 2
        
        