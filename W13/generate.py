## Scripts for generating the text files that we will process in this lecture.

import os
import random
import studentData


## Take JSON from http://www.generatedata.com/ and output it like WebSIS.
# See studentData.py for saved example input.

def websisOut(students):
    f = open("websis.txt", "w")
    f.write("     SPRING TERM 2018-2019      Registration Class List      6.666  U       29-APR-19\n")
    f.write("\n")
    f.write("       6.666       Something or Other                      Somebody McProfessor\n")
    f.write("                   Standard A - F Grading                  32-G000   555-1234\n")
    f.write("\n")
    f.write("     MIT ID    Student Name        Course  Y St  Un Grade  Enrolled Sec Email Address\n")
    f.write("     ------    ------------------  ------  - --- -- -----  -------- --- -------------\n")

    for student in students:
        f.write("     " + str(student["MIT ID"])
                + " " + student["Student Name"]
                + (" " * (23 - len(student["Student Name"]))) + "6 3"
                + "  " + str(student["Y"])
                + " Reg"
                + " 12"
                + "          6.666"
                + "      " + student["Email Address"]
                + "\n")

    f.close()

## From the same kind of data, output random XML grades data.

# Helper function to generate a random grade in a plausible range.
def randomGrade():
    if random.randint(0, 1) == 0:
        return random.randint(90, 100)
    elif random.randint(0, 1) == 0:
        return random.randint(80, 89)
    elif random.randint(0, 1) == 0:
        return random.randint(70, 79)
    elif random.randint(0, 1) == 0:
        return random.randint(60, 69)
    else:
        return random.randint(0, 59)

# Output random XML for one category of grades, given how many items belong to that category.
def xmlSectionOut(students, f, plural, singular, howMany):
    f.write("  <" + plural + ">\n");

    for item in range(1, howMany):
        f.write("    <" + singular + ">\n")
        f.write("      <number>" + str(item) + "</number>\n")

        for student in students:
            f.write("      <student>\n")
            f.write("        <email>" + student["Email Address"] + "</email>\n")
            f.write("        <grade>" + str(randomGrade()) + "</grade>\n")
            f.write("      </student>\n")

        f.write("    </" + singular + ">\n")

    f.write("  </" + plural + ">\n")

# The overall function
def gradesXmlOut(students):
    f = open("grades.xml", "w")
    f.write("<grades>\n")
    xmlSectionOut(students, f, "psets", "pset", 10)
    xmlSectionOut(students, f, "quizzes", "quiz", 4)
    f.write("</grades>\n")
    f.close()

## We also want to demonstrate random grades data as several CSV files.

def csvSectionOut(students, plural, singular, howMany):
    for item in range(1, howMany):
        f = open(os.path.join("grades", singular + str(item) + ".csv"), "w")
        f.write("Email Address,Grade\n")

        for student in students:
            f.write(student["Email Address"] + "," + str(randomGrade()) + "\n")

        f.close()

# The overall function
def gradesCsvOut(students):
    os.mkdir("grades")
    csvSectionOut(students, "psets", "pset", 10)
    csvSectionOut(students, "quizzes", "quiz", 4)


## Run from the command line, we just generate all files.
if __name__ == '__main__':
   websisOut(studentData.students)
   gradesXmlOut(studentData.students)
   gradesCsvOut(studentData.students)
