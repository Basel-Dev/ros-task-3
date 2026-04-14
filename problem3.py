set1 = {"a", "b", "c", "x", "y"}
set2 = {"a", "b", "d", "f", "y"}

def findCommonElements(inputSet1, inputSet2):
    return inputSet1 & inputSet2

print(findCommonElements(set1, set2))