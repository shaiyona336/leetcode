def is_median(nums,indexNeedToGetIn,value):
    if 
    



def findMedianSortedArrays(nums1, nums2):
    currIndex = len(nums1)/2
    size1 = len(nums1)

    while currIndex != 1 and currIndex != size1-1:
        valueToCheck = nums1[currIndex]
        if nums2[currIndex-1+


    if currIndex == 1 or currIndex == size1-1:
        return nums2[len(nums2)/2]





print(binary_search([1,2,3,4,5,6],4))
firstArray = [90,100]
secondArray = [1,2,3,4,5,6,7]
print(findMedianSortedArrays(firstArray,secondArray))

 
firstArray = [6,7,8,9,10]
secondArray = [11,12,13,14]
print(findMedianSortedArrays(firstArray,secondArray))

 
firstArray = [10,40,70,80,90]
secondArray = [20,30,50,60]
print(findMedianSortedArrays(firstArray,secondArray))

