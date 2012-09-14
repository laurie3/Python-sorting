'''
Created on Sep 7, 2012

@author: wma
'''
def partitionList(testList,leftIndex,rightIndex,pivotIndex):
    key=testList[pivotIndex]
    swap(testList,pivotIndex, rightIndex)
    storeIndex=leftIndex
    for i in range(leftIndex,rightIndex):
        if testList[i]<key:
            swap(testList,storeIndex,i)
            storeIndex=storeIndex+1
    swap(testList,storeIndex,rightIndex)
    print testList
    return storeIndex

def swap(testList, indexA, indexB):
    if indexA==indexB:
        pass
    else:
        temp=testList[indexA]
        testList[indexA]=testList[indexB]
        testList[indexB]=temp
        
def quickSorting(testList,left,right):
    if right>left:
        pivotIndex=(right+left)/2
        pivotNewIndex=partitionList(testList,left,right,pivotIndex)
        quickSorting(testList,left,pivotNewIndex-1)
        quickSorting(testList,pivotNewIndex+1,right)
    
if __name__=="__main__":
    testList=[2,3,1,4,6,9,7,0,10,5,8]
    quickSorting(testList,0,len(testList)-1)
    print testList
