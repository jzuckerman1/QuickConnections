exec(open("scripts\methods.py").read())
xPoints = [0, 1, 2, 10, 4, 5]
Xcombinations = list(itTools.permutations(range(len(xPoints)), len(xPoints)))
print(Xcombinations)