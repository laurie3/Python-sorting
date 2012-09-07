'''
Created on Sep 7, 2012

@author: wma
'''

def BubbleSorting(testList, length):
    endItem = 0
    while(endItem<length-1):
        for i in range(length-1, endItem, -1):
            if testList[i]<testList[i-1]:
                temp=testList[i]
                testList[i]=testList[i-1]
                testList[i-1]=temp
        endItem=endItem+1
    return testList
        
if __name__=="__main__":
    testList=[2,3,1,4,6,9,7,0]
    print BubbleSorting(testList,len(testList))
            
        
        
