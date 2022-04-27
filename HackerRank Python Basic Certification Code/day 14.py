class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        x = 101
        y = 0
        for item in self.__elements:
            if item < x:
                x = item
            if item > y:
                y = item
        self.maximumDifference = y - x

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
