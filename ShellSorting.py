'''
Created on Sep 5, 2012

@author: wma
'''
def ShellSorting(testList, length):
    endItem = length
    startItem = length/2
    counter=0
    while(counter!=2):        
        for i in range(startItem+1, endItem):
            flag = False
            key = testList[i]
            j = i-1
            for j in range(i-1,startItem-1,-1):
                if testList[j]>key:
                    testList[j+1] = testList[j]
                    flag = True
                    
                if flag:
                    testList[j] = key
                    flag = False
        startItem = startItem/2
        if startItem == 0:
            counter = counter+1
    return testList
        
        
if __name__ == '__main__':
    testList=[2,3,1,4,6,9,7,0]
    print ShellSorting(testList,len(testList))