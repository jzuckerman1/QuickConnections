import matplotlib.pyplot as pyl
import matplotlib.patches as patches
import itertools as itTools
import datetime
from matplotlib.animation import FuncAnimation

#My scripts
exec(open("scripts\methods.py").read())

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

    print(distanceBetween(pointIt(x1, y1)))

    closestPointMethod, randomMethod, bestMethod, sectorizeMethod = True, True, True, True
    closestPointValues, randomValues, bestValues, sectorizeValues = [], [], [], []
    writeToFile = open("data/pickupBallsResults.txt","a")

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





