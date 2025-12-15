class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        cover_left = [[False for _ in range(n)] for _ in range(n)]]
        cover_right =   [[False for _ in range(n)] for _ in range(n)]]
        cover_top = [[False for _ in range(n)] for _ in range(n)]]
        cover_bot[[False for _ in range(n)] for _ in range(n)]]

        for building in buildings:
            for x in range(building[0]+1,n-1):
                if cover_left[building[1]][x]]:
                    break
                cover_left[building[1][x]] = True
            for x in range(building[0]+1,0,-1):
                if cover_right[building[1]][x]]:
                    break
                cover_left[building[1][x]] = True
            for y in range(building[1]+1,n-1):
                if cover_left[y][building[0]]]:
                    break
                cover_left[building[1][x]] = True
            for y in range(building[0]+1,n-1):
                if cover_left[buildings[y][building[0]]:
                    break
                cover_left[building[1][x]] = True

        for y in range(1,n-1):
            for x in range(1,n-1):
                if cover_left[y][x] and cover_right[y][x] and cover_top[y][x] and cover_bot[y][x]:
                    count += 1

        return count



#the buildings in the frame in the corner cannot be covered
#for every direction, for example left, when there is a building
#then all the buildings after in that direction we mark them
#afterwards we count covered buildings by
#building that are covered from all directions
