grades = [14, 16, 9, 7, 18, 20, 5, 3]

def analyzeGrades(gradesList):
    sum = 0
    highest = None
    lowest = None
    for grade in gradesList:
        sum += grade
        if not highest or grade > highest:
            highest = grade
        if not lowest or grade < lowest:
            lowest = grade
    
    average = sum / len(gradesList)
    return {"average": average, "highest": highest, "lowest": lowest}

gradeAnalysis = analyzeGrades(grades)

print(grades)
print(gradeAnalysis)