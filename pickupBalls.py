import matplotlib.pyplot as plt
import matplotlib.patches as patches
import datetime
from matplotlib.animation import FuncAnimation

#My scripts
exec(open("scripts\methods.py").read())

def resetPlot():
    x1, y1 = x.copy(), y.copy()
    plt.scatter(x1, y1)
    distTravelled = 0
    xLoc, yLoc = [0], [0]
        
if ( __name__ == "__main__"):
    unittest.main()
    
fig, ax = plt.subplots()

DistanceForEachPlot = []

points = 4 #10 is borderline for the max
   
def main_plot(doRandomVal : bool, doClosestPoint : bool, doTotalMin : bool, doSectorize : bool, points : int, loop = False, startPoints = 2) -> None:
    if (loop == True):
        init = 2
        if(startPoints != 2):
            init = startPoints
        for numPoints in range(init, points - 1):
            main_plot(doClosestPoint, doRandomVal, doTotalMin, doSectorize, numPoints)
            
    pauseT = 0.1

    x,y  = list(np.random.uniform(0, 10, points)), list(np.random.uniform(0, 10, points))
    x1, y1 = x.copy(), y.copy()

    plt.scatter(x, y)

    xLoc,yLoc = [0], [0]
    distTravelled = 0

    props = dict(boxstyle='round', facecolor='wheat', alpha=1.0)
    """=========================================================================================================================="""

    #"Dumber" version using whatever random order they are generated in
    if(doRandomVal):
        for i in range(points): #i starts at 0
            plt.axis([0, 10, 0, 10])
            xLoc.append(x1[0])
            yLoc.append(y1[0])
            distTravelled = np.round(distTravelled + hypotenuse(x1[0] - xLoc[i], y1[0] - yLoc[i]))
            x1.remove(xLoc[i+1])
            y1.remove(yLoc[i+1])
            #Plot limits
            plt.xlim = xLoc[i] - xLoc[i-1]
            plt.ylim = yLoc[i] - yLoc[i-1]
            #Plotting
            plt.plot(xLoc, yLoc, color = "green")
            plt.text(0,0,"Distance: " + str(distTravelled), transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox= props)    
            plt.pause(pauseT)
        plt.show()
        DistanceForEachPlot+= ["Random Point Method = " + str(distTravelled)]
        x1, y1 = x.copy(), y.copy()
        plt.scatter(x1, y1)
        distTravelled = 0
        xLoc, yLoc = [0], [0]
        
    """=========================================================================================================================="""
        
    #"Smarter" version using the closest point
    if(doClosestPoint):
        PointListInfo = findCloseWrapper(0, 0, x, y)
        for i in range(points): #i starts at 0
            plt.axis([0, 10, 0, 10])
            xLoc += [PointListInfo[1][i + 1]]
            yLoc += [PointListInfo[2][i + 1]]
            distTravelled = np.round(distTravelled + hypotenuse(xLoc[i + 1] - xLoc[i], yLoc[i + 1] - yLoc[i]),1)       
            #Plot limits
            plt.xlim = xLoc[i] - xLoc[i-1]
            plt.ylim = yLoc[i] - yLoc[i-1]
            #Plotting
            plt.plot(xLoc, yLoc, color = "black")
            plt.text(0,0,"Distance: " + str(distTravelled), transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox= props)    
            plt.pause(pauseT)
        plt.show()
        DistanceForEachPlot+= ["Closest Point Method = " + str(distTravelled)]
        x1, y1 = x.copy(), y.copy()
        plt.scatter(x1, y1)
        distTravelled = 0
        xLoc, yLoc = [0], [0]


    """=========================================================================================================================="""

    #Longest method -> find the shortest distance by plugging and chugging
    #Don't run with more than 10 points
    if(doTotalMin): 
        minimumConnectionMethod = findMinimumConnectWithStart([0] + x1, [0] + y1) 
        for i in range(points): #i starts at 0
            plt.axis([0, 10, 0, 10])
            xLoc.append(minimumConnectionMethod[i + 1][0])
            yLoc.append(minimumConnectionMethod[i + 1][1])
            distTravelled = np.round(distTravelled + hypotenuse(xLoc[i + 1] - xLoc[i], yLoc[i + 1] - yLoc[i]),1)    
            #Plot limits
            plt.xlim = xLoc[i] - xLoc[i-1]
            plt.ylim = yLoc[i] - yLoc[i-1]
            #Plotting
            plt.plot(xLoc, yLoc, color = "black")
            plt.text(0,0,"Distance: " + str(distTravelled), transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox= props)    
            plt.pause(pauseT)
        plt.show()
        DistanceForEachPlot+= ["Total Minimum Method = " + str(distTravelled)]
        x1, y1 = x.copy(), y.copy()
        plt.scatter(x1, y1)
        distTravelled = 0
        xLoc, yLoc = [0], [0]
    """=========================================================================================================================="""

    if(doSectorize): 
        order = fullSectorize(x1, y1, [0, 0])
        plt.axhline(y = (max(y) / 2), color = "blue")
        plt.axvline(x = (max(x) / 2), color = "blue")
        for i in range(points): #i starts at 0
            plt.axis([0, 10, 0, 10])
            xLoc.append(order[i + 1][0])
            yLoc.append(order[i + 1][1])
            distTravelled = np.round(distTravelled + hypotenuse(xLoc[i + 1] - xLoc[i], yLoc[i + 1] - yLoc[i]),1)    
            #Plot limits
            plt.xlim = xLoc[i] - xLoc[i-1]
            plt.ylim = yLoc[i] - yLoc[i-1]
            #Plotting
            plt.plot(xLoc, yLoc, color = "black")
            plt.text(0,0,"Distance: " + str(distTravelled), transform=ax.transAxes, fontsize=14,
                verticalalignment='top',bbox= props)    
            plt.pause(pauseT)
        plt.show()
        DistanceForEachPlot+= ["Quarterizing Data Minimum Connections = " + str(distTravelled)]
        x1, y1 = x.copy(), y.copy()
        plt.scatter(x1, y1)
        distTravelled = 0
        xLoc, yLoc = [0], [0]

    """=========================================================================================================================="""

def recordVals(randomMethod : bool, closestPointMethod : bool, bestMethod : bool, sectorizeMethod : bool) -> None:
    closestPointValues, randomValues, bestValues, sectorizeValues = [], [], [], []
    writeToFile = open("data/pickupBallsResults.txt","a")

    def newLine(): writeToFile.write("\n")#newLine

    #Overall Test in total method.
    trialNum = 1000

    writeToFile.write("---------------------------------------------------------------------------------------\n")
    writeToFile.write("Trial Date: " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") + "\n")
    writeToFile.write("Number of points to connect: " + str(points) + "\n")
    header = "Trial \t \t:"
    if(randomMethod): header += "Random Value \t \t"
    if(closestPointMethod): header += "Closest Point \t \t"
    if(bestMethod): header += "Best Value \t \t"
    if(closestPointMethod): header += "Sectorized Value \t \t"
    writeToFile.write(header + "\n")

    closestPointCorrect = 0
    randomPointCorrect = 0
    sectorizePointCorrect = 0

    for i in range(0, trialNum):
        x,y  = list(np.random.uniform(0, 10, points)), list(np.random.uniform(0, 10, points))
        x1, y1 = x.copy(), y.copy() 
        xLoc,yLoc = [0], [0]
        writeToFile.write(" " + str(i + 1) + "	 	        ")

        if(bestMethod):
            bestValues.append(round(distanceBetween(findMinimumConnectWithStart([0] + x1, [0] + y1)), 3))
            writeToFile.write(str(bestValues[-1])) 
            for i in range(0, 6 - len(str(bestValues[-1]))): 
                writeToFile.write(" ")
            writeToFile.write("	 	          ")

        if(closestPointMethod):
            closePointsInformation = findCloseWrapper(0, 0, x1, y1)
            closestPointValues.append(round(distanceBetween(pointIt(closePointsInformation[1], closePointsInformation[2])), 3))
            writeToFile.write(str(closestPointValues[-1])) 
            for i in range(0, 6 - len(str(closestPointValues[-1]))): 
                writeToFile.write(" ")
            writeToFile.write("	 	     ")
            if(closestPointValues[-1] == bestValues[-1]): closestPointCorrect += 1

        if(randomMethod):
            randomValues.append(round(distanceBetween(pointIt([0] + x1, [0] + y1)), 3))
            writeToFile.write(str(randomValues[-1])) 
            for i in range(0, 6 - len(str(randomValues[-1]))): 
                writeToFile.write(" ")
            writeToFile.write("	 	         ")
            if(randomValues[-1] == bestValues[-1]): randomPointCorrect += 1

        if(sectorizeMethod):
            sectorizeValues.append(round(distanceBetween(fullSectorize(x1, y1, [0, 0])), 3))
            writeToFile.write(str(sectorizeValues[-1])) 
            for i in range(0, 6 - len(str(sectorizeValues[-1]))): 
                writeToFile.write(" ")
            writeToFile.write("\n")
            if(sectorizeValues[-1] == bestValues[-1]): sectorizePointCorrect += 1

    if(bestMethod):
        newLine()
        writeToFile.writelines("Totals: \n")
        writeToFile.writelines("Best Point Average :" + str(round(average(bestValues), 3)) + "\n")
    if(closestPointMethod):
        newLine()
        writeToFile.writelines("Closest Point Average :" + str(round(average(closestPointValues), 3)) + "\n")
        writeToFile.writelines("Correctness Percentage: " + str(round(closestPointCorrect / trialNum, 3) * 100) + "%\n")
    if(randomMethod):
        newLine()
        writeToFile.writelines("Random Point Average :" + str(round(average(randomValues), 3)) + "\n")
        writeToFile.writelines("Correctness Percentage: " + str(round(randomPointCorrect / trialNum) * 100, 3) + "%\n")
    if(sectorizeMethod):
        newLine()
        writeToFile.writelines("Sectorized Point Average :" + str(round(average(sectorizeValues), 3)) + "\n")
        writeToFile.writelines("Correctness Percentage: " + str(round(sectorizePointCorrect / trialNum, 3) * 100) + "%\n")