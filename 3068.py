class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        base=sum(nums)
        valueNode = [(node^k)-node for node in nums]

        positiveValues = [value for value in valueNode if value>0]
        negativeValue = [value for value in valueNode if value<=0]

        if len(positiveValues)%2==0:
            return base+sum(positiveValues)
        
        worstPositive=min(positiveValues)
        if len(negativeValue)>0:
            bestNegative=max(negativeValue)
            valueToRemove = min(worstPositive,-bestNegative)
        else:
            valueToRemove=worstPositive
        return base+sum(positiveValues)-valueToRemove
