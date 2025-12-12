class Solution:
    def countMentions(self, n: int, e: List[List[str]]) -> List[int]:
        z,allMentioned,allUsers,off = Counter(),0,{*range(n)},deque()
        for tm,_,ids in sorted((int(tm),'M' in tp,ids) for tp,tm,ids in e):
            while off and off[-1][0]<=tm: off.pop()
            if ids=='ALL': allMentioned += 1
            elif ids=='HERE': z.update(allUsers-{ide for _,ide in off})
            elif 'id' in ids: z.update(int(ide[2:]) for ide in ids.split())
            else: off.appendleft([tm+60,int(ids)])

        z.update({i:allMentioned for i in range(n)})
        return [*map(z.get,range(n))]