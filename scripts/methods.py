#Imports 
import numpy as np 
import itertools as itTools

def hypotenuse(a : int, b : int) -> int: return np.sqrt((a*a) + (b*b))
    
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
    
def pointIt(xPoints : list, yPoints : list) -> list:
    if (len(xPoints) == 0): return [[]] 
    if not(len(xPoints) == len(yPoints)): return [[]]
    answer = []
    for i in range(len(xPoints)):
        answer += [[xPoints[i], yPoints[i]]]
    return answer

def findCloseWrapper(startX : int, startY : int, xPoints : list, yPoints : list) -> list: 
    """ Connect points by jumping from point to point by the smallest jumps first
    :param startX: Initial x position
    :param startY: Initial y position
    :param xPoints: Possible x positions to go to
    :param yPoints: Possible y positions to go to
    :return Order that jumps from point to point going by what the smallest jump is
    """
    if (len(xPoints) == 0): return [[]] 
    if not(len(xPoints) == len(yPoints)): return [[]]
    order = []
    Xvalues, Yvalues = [startX], [startY]
    xPointsCopy, yPointsCopy = xPoints.copy(), yPoints.copy()
    for i in range(0, len(pointsX)):
        # Find the closest point 
        bestPointInfo = findClose(startX, startY, xPointsCopy, yPointsCopy)
        Xvalues += [bestPointInfo[0]]
        Yvalues += [bestPointInfo[1]]
        order += [xPoints.index(bestPointInfo[0])]
        # Remove it from consideration
        xPointsCopy.remove(bestPointInfo[0])
        yPointsCopy.remove(bestPointInfo[1])
    return [order, Xvalues, Yvalues]

def findMinimumConnectWithStart(xPoints : list, yPoints : list) -> list:
    """ Find the absolute minimum path to connect the points 
    :param xPoints: list of x coordinates to connect
    :param yPoints: list of y coordinates to connect
    :return the list of points in order to give the minimum path length
    """
    if (len(xPoints) == 0): return [[]] 
    if not(len(xPoints) == len(yPoints)): return [[]]
    # Create possible orderings of n elements
    Xcombinations, Ycombinations = list(itTools.permutations(range(len(xPoints)), len(xPoints))), list(itTools.permutations(range(len(yPoints)), len(yPoints)))
    currentMinimum = 9999999
    FirstX, FirstY = 0, 0
    for i in range(len(Xcombinations)):
        # Must begin with the first element (0, 0)
        if(list(Xcombinations[i])[0] != 0):
            break
        # Creates the ordering
        xSet, ySet = list(Xcombinations[i]), list(Ycombinations[i])
        curvalue = 0
        for j in range(len(xSet) - 1):
            # Solve for the length of the given ordering
            xlength = xPoints[xSet[j + 1]] - xPoints[xSet[j]]
            ylength = yPoints[ySet[j + 1]] - yPoints[ySet[j]]
            curvalue += hypotenuse(xlength, ylength)
            # If we already are above the current minimum, stop checking
            if curvalue > currentMinimum: break
        # Rewrite the minimum and order
        if curvalue < currentMinimum: 
            order, currentMinimum = xSet,curvalue
    # Put the points in the correct order
    fullOrder = []
    for i in range(len(xPoints)):
        fullOrder += pointIt([xPoints[order[i]]], [yPoints[order[i]]])
    return fullOrder

def fullSectorize(xPoints : list, yPoints : list, startAt : list) -> list:
    """ Split points into quadrants and solve for the quick connections in each quadrant
    :param xPoints: list of x coordinates to connect
    :param yPoints: list of y coordinates to connect
    :param startAt: the [x, y] to start at.
    :return the list of points in order to give the minimum path length
    """
    if (len(xPoints) == 0): return [[]] 
    if not(len(xPoints) == len(yPoints)): return [[]]
    if not(len(startAt) == 2): return [[]]
    xhalf, yhalf = max(xPoints) / 2, max(xPoints) / 2
    allPoints = pointIt(xPoints, xPoints)
    q1, q2, q3, q4 = sectorize(allPoints, 0, xhalf, 0, yhalf), sectorize(allPoints, xhalf, max(x), 0, yhalf), sectorize(allPoints, 0, xhalf, yhalf, max(y)), sectorize(allPoints,  xhalf, max(x), yhalf, max(y))
    nextUp = q1
    q1 = []
    order = []
    print(q1)
    for i in range(0, 4):
        order += findMinimumConnectWithStart([startAt[0]] + onlyIndex(nextUp, 0), [startAt[1]] + onlyIndex(nextUp, 1)) #only the x/y points of each index
        allPoints = removeElements(allPoints, order)
        #Redefine quarters to adjust for removed points
        if(len(allPoints) == 0):
            break
        else:
            closeWrapperAfterNext = findClose(order[-1][0], order[-1][1], onlyIndex(allPoints, 0), onlyIndex(allPoints, 1)) #finds the next closest point 
            startAt = [closeWrapperAfterNext[0], closeWrapperAfterNext[1]] #x,y for the next closest point
            if (startAt in q2):
                nextUp = q2
                nextUp.remove(startAt)
                q2 = []
            elif (startAt in q3):
                nextUp = q3
                nextUp.remove(startAt)
                q3 = []
            elif (startAt in q4):
                nextUp = q4
                nextUp.remove(startAt)
                q4 = []
    return order