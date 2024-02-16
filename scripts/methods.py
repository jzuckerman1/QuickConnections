#Imports 
import numpy as np 

def hypotenuse(a : int, b : int) -> int: return np.sqrt((a*a) + (b*b))

def findCloseWrapper(startX : int, startY : int, pointsX : list, pointsY : list) -> list: #Formats the same as the others.
    order = []
    Xvalues, Yvalues = [startX], [startY]
    pointsXCopy, pointsYCopy = pointsX.copy(), pointsY.copy()
    for i in range(0, len(pointsX)):
        bestPointInfo = findClose(startX, startY, pointsXCopy, pointsYCopy)
        Xvalues += [bestPointInfo[0]]
        Yvalues += [bestPointInfo[1]]
        order += [pointsX.index(bestPointInfo[0])]
        pointsXCopy.remove(bestPointInfo[0])
        pointsYCopy.remove(bestPointInfo[1])
    return [order, Xvalues, Yvalues]

def findClose(xCur : int, yCur : int, xvals : list, yvals : list) -> list:
    currentClose = hypotenuse(xvals[0] - xCur, yvals[0] - yCur) + 1
    for i in range(len(xvals)):
        val = hypotenuse(xvals[i] - xCur, yvals[i] - yCur)
        if val < currentClose:
            bestX, bestY = xvals[i], yvals[i]
            currentClose = val
    return [bestX, bestY, currentClose]

def distanceBetween(pointList : list) -> int:
    retVal = 0
    for i in range(0, len(pointList) - 1):
        retVal += hypotenuse(pointList[i + 1][0] - pointList[i][0], pointList[i + 1][0] - pointList[i][0])
    return retVal

def average(listOfInts : list) -> int:
    if(listOfInts == []):
        return 0
    sum = 0
    for i in range(0, len(listOfInts)):
        sum += listOfInts[i]
    return (sum / len(listOfInts)) 

def onlyIndex(points : list, index : int) -> list:
    ans = []
    if(len(points) > 0):
        for i in range(0, len(points)):
            ans.append(points[i][index])
    return ans

def removeElements(points : list, toRemove : list) -> list:
    ans = []
    if(len(points) > 0):
        for i in range(0, len(points)):
            if(points[i] not in toRemove):
                ans.append(points[i])
    return ans

def sectorize(points : list, lowBoundX : int, highBoundX : int, lowBoundY : int, highBoundY : int) -> list:
        copy = []
        if(len(points) > 0):
            for i in range(len(points)): # 0 -> length - 1
               if((points[i][0] <= highBoundX and points[i][0] >= lowBoundX) and(points[i][1] <= highBoundY and points[i][1] >= lowBoundY)):
                   copy.append(points[i])
        return copy

def findMinimumConnectWithStart(xPoints : list, yPoints : list) -> list:
    if (len(xPoints) == 0): return [[]]
    if not(len(xPoints) == len(yPoints)): return [[]]
    Xcombinations, Ycombinations = list(itTools.permutations(range(len(xPoints)), len(xPoints))), list(itTools.permutations(range(len(yPoints)), len(yPoints)))
    currentMinimum = 9999999
    FirstX, FirstY = 0, 0
    for i in range(len(Xcombinations)):
        if(list(Xcombinations[i])[0] != 0):
            break
        xSet, ySet = list(Xcombinations[i]), list(Ycombinations[i])
        curvalue = 0
        for j in range(len(xSet) - 1):
            xlength = xPoints[xSet[j + 1]] - xPoints[xSet[j]]
            ylength = yPoints[ySet[j + 1]] - yPoints[ySet[j]]
            curvalue += hypotenuse(xlength, ylength)
            if curvalue > currentMinimum: break
        if curvalue < currentMinimum: 
            order, currentMinimum = xSet,curvalue
    fullOrder = []
    for i in range(len(xPoints)):
        fullOrder += pointIt([xPoints[order[i]]], [yPoints[order[i]]])
    return fullOrder


#"""
#Goal: Split the data in half and treat each segment as it's own stuff. 
#Find the quickest way to connect points in one section, then find the closest section after.
#"""
def fullSectorize(x1 : list, y1 : list, startAt : list) -> list:
    xhalf, yhalf = max(x1) / 2, max(y1) / 2
    allPoints = pointIt(x1, y1)
    q1, q2, q3, q4 = sectorize(allPoints, 0, xhalf, 0, yhalf), sectorize(allPoints, xhalf, max(x), 0, yhalf), sectorize(allPoints, 0, xhalf, yhalf, max(y)), sectorize(allPoints,  xhalf, max(x), yhalf, max(y))
    next = q1
    q1 = []
    order = []
    print(q1)
    for i in range(0, 4):
        order += findMinimumConnectWithStart([startAt[0]] + onlyIndex(next, 0), [startAt[1]] + onlyIndex(next, 1)) #only the x/y points of each index
        allPoints = removeElements(allPoints, order)
        #Redefine quarters to adjust for removed points
        if(len(allPoints) == 0):
            break
        else:
            closeWrapperAfterNext = findClose(order[-1][0], order[-1][1], onlyIndex(allPoints, 0), onlyIndex(allPoints, 1)) #finds the next closest point 
            startAt = [closeWrapperAfterNext[0], closeWrapperAfterNext[1]] #x,y for the next closest point
            if (startAt in q2):
                next = q2
                next.remove(startAt)
                q2 = []
            elif (startAt in q3):
                next = q3
                next.remove(startAt)
                q3 = []
            elif (startAt in q4):
                next = q4
                next.remove(startAt)
                q4 = []
    return order