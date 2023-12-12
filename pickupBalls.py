import numpy as np 
import matplotlib.pyplot as pyl
import matplotlib.patches as patches
import itertools as itTools
import datetime
from matplotlib.animation import FuncAnimation

fig, ax = pyl.subplots()

DistanceForEachPlot = []

points = 4 #10 is borderline for the max
for points in range(3, 8):
    pauseT = 0.1

    x,y  = list(np.random.uniform(0, 10, points)), list(np.random.uniform(0, 10, points))
    x1, y1 = x.copy(), y.copy()

    pyl.scatter(x, y)

    xLoc,yLoc = [0], [0]
    distTravelled = 0

    def pointIt(xList : list, yList : list) -> list:
        answer = []
        for i in range(len(xList)):
            answer += [[xList[i], yList[i]]]
        return answer

    def resetPlot():
        x1, y1 = x.copy(), y.copy()
        pyl.scatter(x1, y1)
        distTravelled = 0
        xLoc, yLoc = [0], [0]

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

    props = dict(boxstyle='round', facecolor='wheat', alpha=1.0)

    #"Smarter" version using the closest point
    if(False):
        PointListInfo = findCloseWrapper(0, 0, x, y)
        for i in range(points): #i starts at 0
            pyl.axis([0, 10, 0, 10])
            xLoc += [PointListInfo[1][i + 1]]
            yLoc += [PointListInfo[2][i + 1]]
            distTravelled = np.round(distTravelled + hypotenuse(xLoc[i + 1] - xLoc[i], yLoc[i + 1] - yLoc[i]),1)       
            #Plot limits
            pyl.xlim = xLoc[i] - xLoc[i-1]
            pyl.ylim = yLoc[i] - yLoc[i-1]
            #Plotting
            pyl.plot(xLoc, yLoc, color = "black")
            pyl.text(0,0,"Distance: " + str(distTravelled), transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox= props)    
            pyl.pause(pauseT)
        pyl.show()
        DistanceForEachPlot+= ["Closest Point Method = " + str(distTravelled)]
        x1, y1 = x.copy(), y.copy()
        pyl.scatter(x1, y1)
        distTravelled = 0
        xLoc, yLoc = [0], [0]

    """=========================================================================================================================="""

    #"Dumber" version using whatever random order they are generated in
    if(False):
        for i in range(points): #i starts at 0
            pyl.axis([0, 10, 0, 10])
            xLoc.append(x1[0])
            yLoc.append(y1[0])
            distTravelled = np.round(distTravelled + hypotenuse(x1[0] - xLoc[i], y1[0] - yLoc[i]))
            x1.remove(xLoc[i+1])
            y1.remove(yLoc[i+1])
            #Plot limits
            pyl.xlim = xLoc[i] - xLoc[i-1]
            pyl.ylim = yLoc[i] - yLoc[i-1]
            #Plotting
            pyl.plot(xLoc, yLoc, color = "green")
            pyl.text(0,0,"Distance: " + str(distTravelled), transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox= props)    
            pyl.pause(pauseT)
        pyl.show()
        DistanceForEachPlot+= ["Random Point Method = " + str(distTravelled)]
        x1, y1 = x.copy(), y.copy()
        pyl.scatter(x1, y1)
        distTravelled = 0
        xLoc, yLoc = [0], [0]


    """=========================================================================================================================="""

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
            #print(pointIt(xPoints,yPoints))
            #print(pointIt(xSet,ySet))
            curvalue = 0
            for j in range(len(xSet) - 1):
                #print("Finding difference from: ")
                #print([[xPoints[xSet[j + 1]], yPoints[ySet[j + 1]]], [xPoints[xSet[j]], yPoints[ySet[j]]]])
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

    #Longest method -> find the shortest distance by plugging and chugging
    #Don't run with many points...
    if(False): 
        minimumConnectionMethod = findMinimumConnectWithStart([0] + x1, [0] + y1) 
        for i in range(points): #i starts at 0
            pyl.axis([0, 10, 0, 10])
            xLoc.append(minimumConnectionMethod[i + 1][0])
            yLoc.append(minimumConnectionMethod[i + 1][1])
            distTravelled = np.round(distTravelled + hypotenuse(xLoc[i + 1] - xLoc[i], yLoc[i + 1] - yLoc[i]),1)
            #x1.remove(xLoc[i+1])
            #y1.remove(yLoc[i+1])        
            #Plot limits
            pyl.xlim = xLoc[i] - xLoc[i-1]
            pyl.ylim = yLoc[i] - yLoc[i-1]
            #Plotting
            pyl.plot(xLoc, yLoc, color = "black")
            pyl.text(0,0,"Distance: " + str(distTravelled), transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox= props)    
            pyl.pause(pauseT)
        pyl.show()
        DistanceForEachPlot+= ["Total Minimum Method = " + str(distTravelled)]
        x1, y1 = x.copy(), y.copy()
        pyl.scatter(x1, y1)
        distTravelled = 0
        xLoc, yLoc = [0], [0]
    """=========================================================================================================================="""

    def sectorize(points : list, lowBoundX : int, highBoundX : int, lowBoundY : int, highBoundY : int) -> list:
        copy = []
        if(len(points) > 0):
            for i in range(len(points)): # 0 -> length - 1
               if((points[i][0] <= highBoundX and points[i][0] >= lowBoundX) and(points[i][1] <= highBoundY and points[i][1] >= lowBoundY)):
                   copy.append(points[i])
        return copy

    def onlyIndex(points : list, index : int) -> list:
        ans = []
        if(len(points) > 0):
            for i in range(0, len(points)):
                ans.append(points[i][index])
        return ans

    def remove_elements(points : list, toRemove : list) -> list:
        ans = []
        if(len(points) > 0):
            for i in range(0, len(points)):
                if(points[i] not in toRemove):
                    ans.append(points[i])
        return ans
    assert(remove_elements([1, 2, 3, 4, 5], [2, 3, 4]) == ([1, 5]))

    x1, y1 = x.copy(), y.copy()
    pyl.scatter(x1, y1)
    distTravelled = 0
    xLoc, yLoc = [0], [0]

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
            allPoints = remove_elements(allPoints, order)
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

    if(False): 
        order = fullSectorize(x1, y1, [0, 0])
        pyl.axhline(y = (max(y) / 2), color = "blue")
        pyl.axvline(x = (max(x) / 2), color = "blue")
        for i in range(points): #i starts at 0
            pyl.axis([0, 10, 0, 10])
            xLoc.append(order[i + 1][0])
            yLoc.append(order[i + 1][1])
            distTravelled = np.round(distTravelled + hypotenuse(xLoc[i + 1] - xLoc[i], yLoc[i + 1] - yLoc[i]),1)
            #x1.remove(xLoc[i+1])
            #y1.remove(yLoc[i+1])        
            #Plot limits
            pyl.xlim = xLoc[i] - xLoc[i-1]
            pyl.ylim = yLoc[i] - yLoc[i-1]
            #Plotting
            pyl.plot(xLoc, yLoc, color = "black")
            pyl.text(0,0,"Distance: " + str(distTravelled), transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox= props)    
            pyl.pause(pauseT)
        pyl.show()
        DistanceForEachPlot+= ["Quarterizing Data Minimum Connections = " + str(distTravelled)]
        x1, y1 = x.copy(), y.copy()
        pyl.scatter(x1, y1)
        distTravelled = 0
        xLoc, yLoc = [0], [0]

    """=========================================================================================================================="""

    # print(pointIt(x1, y1))
    # print(DistanceForEachPlot)


    def distanceBetween(pointList : list) -> int:
        retVal = 0
        for i in range(0, len(pointList) - 1):
            retVal += hypotenuse(pointList[i + 1][0] - pointList[i][0], pointList[i + 1][0] - pointList[i][0])
        return retVal

    def average(listOfInts : list) -> int:
        sum = 0
        for i in range(0, len(listOfInts)):
            sum += listOfInts[i]
        return (sum / len(listOfInts))

    print(distanceBetween(pointIt(x1, y1)))

    closestPointMethod, randomMethod, bestMethod, sectorizeMethod = True, True, True, True
    closestPointValues, randomValues, bestValues, sectorizeValues = [], [], [], []
    writeToFile = open("pickupBallsResults.txt","a")

    def newLine(): writeToFile.write("\n")#newLine

    #Overall Test in total method.
    trialNum = 1000
    
    writeToFile.write("---------------------------------------------------------------------------------------\n")
    writeToFile.write("Trial Date: " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") + "\n")
    writeToFile.write("Number of points to connect: " + str(points) + "\n")
    writeToFile.write("Trial \t \t Best Value \t \t Closest Point \t \t Random Value \t \t Sectorized Value\n")

    def round(num):
        return np.round(num, 3)
    closestPointCorrect = 0
    randomPointCorrect = 0
    sectorizePointCorrect = 0

    for i in range(0, trialNum):
        x,y  = list(np.random.uniform(0, 10, points)), list(np.random.uniform(0, 10, points))
        x1, y1 = x.copy(), y.copy() 
        xLoc,yLoc = [0], [0]
        writeToFile.write(" " + str(i + 1) + "	 	        ")

        if(bestMethod):
            bestValues.append(round(distanceBetween(findMinimumConnectWithStart([0] + x1, [0] + y1))))
            writeToFile.write(str(bestValues[-1])) 
            for i in range(0, 6 - len(str(bestValues[-1]))): 
                writeToFile.write(" ")
            writeToFile.write("	 	          ")

        if(closestPointMethod):
            closePointsInformation = findCloseWrapper(0, 0, x1, y1)
            closestPointValues.append(round(distanceBetween(pointIt(closePointsInformation[1], closePointsInformation[2]))))
            writeToFile.write(str(closestPointValues[-1])) 
            for i in range(0, 6 - len(str(closestPointValues[-1]))): 
                writeToFile.write(" ")
            writeToFile.write("	 	     ")
            if(closestPointValues[-1] == bestValues[-1]): closestPointCorrect += 1

        if(randomMethod):
            randomValues.append(round(distanceBetween(pointIt([0] + x1, [0] + y1))))
            writeToFile.write(str(randomValues[-1])) 
            for i in range(0, 6 - len(str(randomValues[-1]))): 
                writeToFile.write(" ")
            writeToFile.write("	 	         ")
            if(randomValues[-1] == bestValues[-1]): randomPointCorrect += 1

        if(sectorizeMethod):
            sectorizeValues.append(round(distanceBetween(fullSectorize(x1, y1, [0, 0]))))
            writeToFile.write(str(sectorizeValues[-1])) 
            for i in range(0, 6 - len(str(sectorizeValues[-1]))): 
                writeToFile.write(" ")
            writeToFile.write("\n")
            if(sectorizeValues[-1] == bestValues[-1]): sectorizePointCorrect += 1

    newLine()
    writeToFile.writelines("Totals: \n")
    writeToFile.writelines("Best Point Average :" + str(round(average(bestValues))) + "\n")
    newLine()
    writeToFile.writelines("Closest Point Average :" + str(round(average(closestPointValues))) + "\n")
    writeToFile.writelines("Correctness Percentage: " + str(round(closestPointCorrect / trialNum) * 100) + "%\n")
    newLine()
    writeToFile.writelines("Random Point Average :" + str(round(average(randomValues))) + "\n")
    writeToFile.writelines("Correctness Percentage: " + str(round(randomPointCorrect / trialNum) * 100) + "%\n")
    newLine()
    writeToFile.writelines("Sectorized Point Average :" + str(round(average(sectorizeValues))) + "\n")
    writeToFile.writelines("Correctness Percentage: " + str(round(sectorizePointCorrect / trialNum) * 100) + "%\n")





