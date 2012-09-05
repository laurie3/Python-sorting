def InsertSorting(testList, length):
        
    for i in range(1, length):
        flag = False
        key = testList[i]
        j=i-1
        for j in range(i-1,-1,-1):
            if testList[j]>key:
                testList[j+1] = testList[j]
                flag = True
                #if it finds a place to insert turn the flag to True for future control
            if flag:
                testList[j] = key
                flag = False
				#Important to set the flag back once finished inserting item at the end of the list
    return testList

if __name__ == '__main__':
    testList=[2,3,1,4,6,9,7,0]
    print InsertSorting(testList,len(testList))
    
    
    
