class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d= defaultdict(int)

        for i in points:
            d[tuple(i)]=(math.sqrt((i[0]**2) + (i[1]**2)))
        print(d)

        h=[]
        res=[]

        for ke,val in d.items():
            if len(h)<k:
                heapq.heappush(h,(-val,ke))
            else:
                if val < h[0][0] * -1:
                    heapq.heappop(h)
                    heapq.heappush(h,(-val,ke))

        while len(h):
            elem=heapq.heappop(h)
            res.append(list(elem[1]))



        print(res)
        return res
        