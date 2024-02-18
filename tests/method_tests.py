# Imports
exec(open("scripts\methods.py").read())
import unittest

class FunctionTests(unittest.TestCase): 
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(7,24),25)
        self.assertNotEqual(hypotenuse(7,24),1)
        
    def test_average(self):
        self.assertEqual(average([]), 0)
        self.assertEqual(average([1, 2, 3]), 2)
        self.assertEqual(average([2, 2, 2]), 2)
        
    def test_findClose(self):
        xPoints = [1, 3, 5]
        yPoints = [0, 2, 4]
        self.assertEqual(findClose(0, 0, xPoints, yPoints), [1, 0, hypotenuse(1, 0)])
        xPoints2 = [4, 6, 9]
        yPoints2 = [3, 2, 8]
        self.assertEqual(findClose(0, 0, xPoints2, yPoints2), [4, 3, hypotenuse(4, 3)])
    
    def test_onlyIndex(self):
        nestedList = [[0, 1], [0, 2], [0, 3], [2, 3], [4, 5]]
        self.assertEqual(onlyIndex(nestedList, 0), [0, 0, 0, 2, 4])
        self.assertEqual(onlyIndex(nestedList, 1), [1, 2, 3, 3, 5])
        
    def test_removeElements(self):
        self.assertEqual(removeElements([1, 2, 3, 4, 5], [2, 3, 4]), ([1, 5]))
        self.assertEqual(removeElements([1, 2, 3, 4, 5], []), ([1, 2, 3, 4, 5]))
        self.assertEqual(removeElements([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), ([]))
        
    def test_sectorize(self):
        points = [[1, 2], [3, 4], [5, 6], [2, 2], [7, 5], [-2, 0], [10, 10]]
        self.assertEqual(sectorize(points, 0, 5, 0, 5), [[1, 2], [3, 4], [2, 2]])
        self.assertEqual(sectorize(points, -5, 1, 8, 10), [])
        self.assertEqual(sectorize(points, 8, 12, 0, 20), [[10, 10]])
        
    def test_pointIt(self):
        xValues, yValues = [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]
        self.assertEqual(pointIt(xValues, yValues), [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]])
        self.assertEqual(pointIt(xValues[:3], yValues[:3]), [[1, 5], [2, 4], [3, 3]])
        self.assertEqual(pointIt([], []), [[]])
        
        
    
        
if ( __name__ == "__main__"):
    unittest.main()