name = input("Enter student name \n")
labGrade = int(input("Enter lab grade \n"))
midGrade = int(input("Enter midterm grade \n"))
finalGrade = int(input("Enter final grade \n"))

totalGrade = labGrade*0.25 + midGrade*0.35 + finalGrade*0.40

print("Name : " + str(name) + "\nLab grade : " + str(labGrade) + "\nMidterm grade : " + str(midGrade) + "\nFinal grade : " + str(finalGrade) + "\nTotal grade :" + str(totalGrade))
