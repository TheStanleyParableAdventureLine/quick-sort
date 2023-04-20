#Sam Bowles 18/04/2023
#finally got it to work on 19/04/2023
#optimisations made on 20/04/2023

myList = [5, 3, 8, 9, 6, 2, 7, 3, 1, 4]

myOtherList = [19, 24, 6, 13, 21, 25, 9, 9, 30, 2, 22, 25, 22, 9, 30, 10, 22, 22, 17, 11, 22, 1, 4, 3, 28, 25, 2, 24, 30, 0]

myOtherOtherList = [20, 48, 6, 41, 40, 17, 28, 50, 10, 49, 36, 9, 27, 48, 17, 9, 33, 32, 41, 38, 29, 14, 47, 30, 7, 30, 16, 6, 36,
                    12, 20, 2, 44, 16, 16, 3, 29, 4, 36, 7, 41, 25, 2, 30, 3, 3, 26, 44, 9, 25
                    ]

finalList = [9, 47, 11, 56, 26, 55, 88, 78, 31, 16, 96, 62, 45, 15, 39, 25, 39, 2, 37, 7, 91, 6, 58, 96, 70, 44, 13, 44, 51, 41, 6,
             70, 26, 88, 13, 12, 2, 53, 56, 8, 7, 49, 10, 24, 50, 29, 89, 45, 29, 16, 45, 3, 54, 8, 35, 32, 28, 70, 55, 80, 94, 72,
             28, 88, 20, 77, 100, 94, 76, 52, 93, 51, 62, 72, 81, 77, 89, 26, 9, 82, 55, 39, 38, 41, 23, 54, 19, 23, 4, 32, 64, 88,
             1, 54, 75, 86, 54, 81, 94, 28
             ]

listOfLists = [myList, myOtherList, myOtherOtherList, finalList]

steps = 0

#function to swap the indexes of two items in a list
def swapIndex(theList, indexOne, indexTwo):
    temp = theList[indexOne]
    theList[indexOne] = theList[indexTwo]
    theList[indexTwo] = temp

#function to choose the pivot as the median of three values from the list
#this could probably be written much more efficiently than it is
def choosePivot(theList):
    
    if len(theList) < 3:
        return 0

    #select three items from the list from the start, middle, and end
    index1 = 0
    index2 = (len(theList) - 1) // 2
    index3 = len(theList) - 1

    tempList = [theList[index1], theList[index2], theList[index3]]

    #check for the median value in the list
    for index in range(len(tempList)):
        
        selectedItem = tempList[index]
        
        if selectedItem != max(tempList) and selectedItem != min(tempList):
            
            #return the index of the item
            return [index1, index2, index3][index]

    #if the median occurs more than once, choose a repeated value
    for index in range(len(tempList)):
        
        selectedItem = tempList[index]

        for otherIndex in range(len(tempList)):
            
            #if the item is repeated
            if index != otherIndex and tempList[index] == tempList[otherIndex]:
                
                #return the index of the item
                return [index1, index2, index3][index]

#recursive quick sort for a list of integer numbers
def quickSortInts(theListRef):

    #increment steps variable
    global steps
    steps += 1

    #if the list contains less than two items, it doesn't need sorting
    if len(theListRef) < 2:
        return theListRef
    
    else:
        
        #print("sorting " + str(theListRef))
    
        theList = theListRef    #make a copy of the list so we don't mess with the original list
        
        #find the pivot and move it to the end of the list
        pivot = choosePivot(theList)
        swapIndex(theList, pivot, len(theList) - 1)
        pivot = len(theList) - 1

        leftItemIndex = 0
        rightItemIndex = pivot - 1
        
        while True:

            #find index of first item from the right that is smaller than the pivot
            while rightItemIndex > -1:
                if theList[rightItemIndex] > theList[pivot]:
                    rightItemIndex -= 1
                else:
                    break

            #find index of first item from the left that is larger than the pivot
            while leftItemIndex < pivot:
                if theList[leftItemIndex] <= theList[pivot]:
                    leftItemIndex += 1
                else:
                    break

            #detects if we have found the right place for the pivot
            if leftItemIndex >= rightItemIndex:
                break

            #otherwise, the indexes need to be swapped
            swapIndex(theList, leftItemIndex, rightItemIndex)
            #print(theList)

        #this places the pivot in the correct place in the list
        swapIndex(theList, pivot, leftItemIndex)
        temp = pivot
        pivot = leftItemIndex
        leftItemIndex = temp

        #split the list into two sublists
        subListOne = theList[0 : pivot]
        subListTwo = theList[pivot + 1 : len(theList)]

        #print("sublist 1: " + str(subListOne))
        #print("sublist 2: " + str(subListTwo))
        #print("pivot:     " + str(theList[pivot]))

        #quick sort each sublist and return them in order
        return quickSortInts(subListOne) + [theList[pivot]] + quickSortInts(subListTwo)

#function to verify whether a list is sorted or not
def verifySort(theList):

    for index in range(len(theList) - 1):
        if theList[index] > theList[index + 1]:
            print("sort failed!")
            return

    print("sort success!")

for thisList in listOfLists:
    mySortedList = quickSortInts(thisList)
    verifySort(mySortedList)
    print(mySortedList)
    print("steps: " + str(steps))
