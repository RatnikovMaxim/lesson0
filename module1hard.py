gradesList = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
studentsSet = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_mid = ([(sum(gradesList[0])/len(gradesList[0])),
           (sum(gradesList[1])/len(gradesList[1])),
           (sum(gradesList[2])/len(gradesList[2])),
           (sum(gradesList[3])/len(gradesList[3])),
           (sum(gradesList[4])/len(gradesList[4]))])
print(grades_mid)
studentsSort = sorted(studentsSet)
print(studentsSort)
dict_ = dict(zip(studentsSort, grades_mid))
print(dict_)