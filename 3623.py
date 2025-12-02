class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        output = 0
        x_for_y = defaultdict(int)
        how_many_per_y = []
        how_many_couples = 0
        MOD = 10**9 + 7

        for x,y in points:
            x_for_y[y] += 1
        
        for count in x_for_y.values():
            if count >= 2:
                curr_amount_couples =  (count*(count-1))//2
                how_many_couples += curr_amount_couples
                how_many_per_y.append(curr_amount_couples)

        for horizontal_line_amount_couples in how_many_per_y:
            how_many_couples -= horizontal_line_amount_couples
            output += horizontal_line_amount_couples*how_many_couples
            output = output % MOD
            
        return output





#we need to find how many horizontal trapezoid there is
#define horizontal trapezoid as ht
#4 points consider ht if each two has same y but different
#than the other two
#what is the fastest way to find this groups?
#for every two points with same y, we can find all groups of other two dots
#with different y but same y between each other
#need to group the dots based on y
#then for every group choose two from this group
#and for each other group
#choose two
#example:
#formula y: x1, x2, x3...
#1: 0,2,4
#3: 1,3,5
#5: 2,4,6,8
#7: 3,4,5,6

#first calculate first group choose 2 from 3 => 3
#then each of this can make a square with y=3 so 3*3
#same with y=5,y=7, so overall=3*3+3*6+3*6=45
#then y=3 with y=5,y=7
#so 3*6+3*6
#so need to calculate overrall groups, and how many in each y
#and every iteration remove from overall current group
#and multiply it with size of current group y to add to
#output sum
