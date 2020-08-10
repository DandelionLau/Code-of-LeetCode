class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    x1, y1 = points[i][0], points[i][1]
                    x2, y2 = points[j][0], points[j][1]
                    x3, y3 = points[k][0], points[k][1]
                    a = self.distance(x1, y1, x2, y2)
                    b = self.distance(x1, y1, x3, y3)
                    c = self.distance(x3, y3, x2, y2)
                    res = max(res, self.getArea(a, b, c))
        return res


    def getArea(self, a, b, c):
        p = (a + b + c) / 2
        return math.sqrt(abs(p * (p - a) * (p - b) * (p - c)))

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
