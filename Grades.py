grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = list(students)
a = (sum(grades[0]) / (len(grades[0])))
b = (sum(grades[1]) / (len(grades[1])))
c = (sum(grades[2]) / (len(grades[2])))
d = (sum(grades[3]) / (len(grades[3])))
e = (sum(grades[4]) / (len(grades[4])))
sorted_students = sorted(my_list, reverse = False)
students_grades = {}
students_grades.update({(sorted_students[0]) : a,
                        (sorted_students[1]) : b,
                        (sorted_students[2]) : c,
                        (sorted_students[3]) : d,
                        (sorted_students[4]) : e})
print(students_grades)