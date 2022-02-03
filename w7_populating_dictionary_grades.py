# week 7 - Populating a Dictionary
def read_grades(gradefile):
    ''' (file open for reading) -> dict of {float: list of str}

    Read the grades from gradefile and return a dictionary where
    each key is a grade and each value is the list of ids of students
    who earned that grade.

    Precondition: gradefile starts with a header that contains
    no blank lines, then has a blank line, and then lines containing
    a student number and a grade.


    >>> gradesfile = open('C:/Users/luiza/AppData/Local/Programs/Python/Python310/w7_grades.txt')
    >>> read_grades(gradesfile)
    {77.5: ['0052', '1311'],
     37.5: ['0072'],
     62.5: ['0144', '0417', '0583', '1078'],
     72.5: ['0162'],
    100.0: ['0173'],
     55.0: ['0190', '1389'],
     95.0: ['0196', '0480'],
     82.5: ['0225'],
     97.5: ['0268'],
     57.5: ['0306', '0941'],
     70.0: ['0403', '0645'],
     40.0: ['0455'],
     25.0: ['0481', '0491'],
     50.0: ['0544'],
     90.0: ['0587'],
     92.5: ['0673', '0794'],
     85.0: ['0689', '1376', '1377'],
     47.5: ['0988'],
     45.0: ['1242'],
     67.5: ['1388']}
    
    '''

    # Skip over the header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()


    # Read the grades, accumulating them into a dict.

    grade_to_ids = {}
    line = gradefile.readline()

    while line != '':
        student_id = line[:4]
        grade = float(line[4:].strip())

        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id]
        else:
            grade_to_ids[grade].append(student_id)

        line = gradefile.readline()
    return grade_to_ids


#----------------------w7_grades.txt
#* Assignment 1 grades
#* Columns:
#* id grade
#
#0052 77.5
#0072 37.5
#0144 62.5
#0162 72.5
#0173 100.0
#0190 55.0
#0196 95.0
#0225 82.5
#0268 97.5
#0306 57.5
#0403 70.0
#0417 62.5
#0455 40.0
#0480 95.0
#0481 25.0
#0491 25.0
#0544 50.0
#0583 62.5
#0587 90.0
#0645 70.0
#0673 92.5
#0689 85.0
#0794 92.5
#0941 57.5
#0988 47.5
#1078 62.5
#1242 45.0
#1311 77.5
#1376 85.0
#1377 85.0
#1388 67.5
#1389 55.0


