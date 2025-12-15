class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        index = 1
        current_part = 1
        size = len(prices)
        if size == 0:
            return 0

        while index < size:
            if prices[index]+1==prices[index-1] or current_part == 0:
                current_part += 1
            else:
                count += (current_part+1)*current_part//2
                current_part = 1
            index += 1

        count += (current_part+1)*current_part//2
        

        return count






#every area of smooth descent period is also smooth descent period
#so lets say for example with hav e [1,2,3,4], we can choose
#at the start only 1 every time, so [1],[2],[3],[4]
#and then 2, so overrall:
#4+3+2+1
#so in general: l+(l-1)+...+1=(l+1)*l/2
