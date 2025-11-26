class segmentTree:
    def __init__(self, data):
        sizeData = len(data)
        size = 1 << (math.ceil(math.log2(sizeData))+1)
        self.tree = [-1] * size
        #build tree
        self.build(1,0,sizeData-1,data)

    def build(self,indexTree,left,right,data):
        if left == right:
            self.tree[indexTree] = data[left]
        else:
            mid = (left+right)//2
            self.build(indexTree*2,left,mid,data)
            self.build(indexTree*2+1,mid+1,right,data)
            self.tree[indexTree] = max(self.tree[indexTree*2],self.tree[indexTree*2+1])


    def update(self,indexTree, indexOriginal, left,right,value):
        if left == right:
            self.tree[indexTree] = value
        else:
            mid = (left+right)//2
            if indexOriginal <= mid:
                self.update(indexTree*2, indexOriginal, left, mid, value)
            else:
                self.update(indexTree*2+1,indexOriginal,mid+1,right,value)
            self.tree[indexTree]= max(self.tree[indexTree*2],self.tree[indexTree*2+1])


    def find(self, indexTree, left, right, value):
        if self.tree[indexTree] < value:
            return -1
        if left == right:
            return left
        mid = (left+right)//2
        if self.tree[indexTree*2] >= value:
            return self.find(indexTree*2,left,mid,value)
        else:
            return self.find(indexTree*2+1,mid+1,right,value)



class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        size = len(baskets)
        tree = segmentTree(baskets)

        for index in range(size):
            fitBasket = tree.find(1,0,size-1,fruits[index])
            if fitBasket == -1:
                count += 1
            else:
                tree.update(1,fitBasket,0,size-1,-1)

        return count


        
