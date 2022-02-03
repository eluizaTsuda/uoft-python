import tkinter.filedialog
import w6_developing_program_grade

# open file w6_grades.txt
a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename, 'r')


#for line in a1_file:
#    print(line)

# write file w6_grades_histogramn.txt
a1_histfilename = tkinter.filedialog.asksaveasfilename()
a1_histfile = open(a1_histfilename, 'w')

# Read the grades into a list
grades = w6_developing_program_grade.read_grades(a1_file)

# Count the grades per range.
range_counts = w6_developing_program_grade.count_grade_ranges(grades)

print(range_counts)

# Write the histogram to the file.

w6_developing_program_grade.write_histogram(range_counts, a1_histfile)

a1_file.close()
a1_histfile.close()
