class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        sum = 0
        candies = [1]*len(ratings)
        ratingToChild = {}
        needsToBeBiggerThanFromLeft = 0

        for ratingIndex in range(0,len(ratings)):
            ratingCurrChild = ratings[ratingIndex]
            if ratingCurrChild not in ratingToChild:
                ratingToChild[ratingCurrChild] = [ratingIndex]
            else:
                ratingToChild[ratingCurrChild].append(ratingIndex)

        ratingToChild = dict(sorted(ratingToChild.items()))

        for rating in ratingToChild:
            for childIndex in ratingToChild[rating]:
                needsToBeBiggerThanFromLeft = 0
                if (childIndex > 0 and ratings[childIndex] > ratings[childIndex-1] and candies[childIndex] <= candies[childIndex-1]):
                    candies[childIndex] = candies[childIndex-1] + 1
                    needsToBeBiggerThanFromLeft = candies[childIndex-1] + 1
                if (childIndex < len(ratings) - 1 and ratings[childIndex] > ratings[childIndex+1] and candies[childIndex] <= candies[childIndex+1]):
                    candies[childIndex] = candies[childIndex+1] + 1
                    if (needsToBeBiggerThanFromLeft > candies[childIndex]):
                        candies[childIndex] = needsToBeBiggerThanFromLeft

                

        for candy in candies:
            sum += candy

        return sum



solution = Solution()
print(solution.candy([5,1,1,1,10,2,1,1,1,3]))