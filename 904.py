class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        currFruits = 0
        amountTypes = defaultDict(int)
        left = 0

        for right,value in enumerate(fruits):
            amountTypes[value] += 1
            currFruits += 1

            while len(amountTypes) > 2:
                amountTypes[fruits[left]] -= 1
                if amountTypes[fruits[left]] == 0:
                    del amountTypes[fruits[left]]
                currFruits -= 1
                left += 1

            maxFruits = max(maxFruits,currFruits)

        return maxFruits

