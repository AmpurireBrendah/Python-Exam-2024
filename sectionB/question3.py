

     
#3(iii)
marks_scored=float(input("Enter the student score in the subject (0-100):"))
#Validate the marks within a plausible range(0-100)
if 0 <= marks_scored <=100:
    if marks_scored >=90:
        grade="A"
        print("Grade", grade)
    elif marks_scored >=80:
        grade="B"
        print("Grade",grade)
    elif marks_scored >=70:
        grade="C"
        print("Grade",grade)
    elif marks_scored >=60:
        grade="D"
        print("Grade",grade)
    elif marks_scored >=50:
        grade="E"
        print("Grade",grade)
    else:
        grade="F"
        print("Grade",grade)

#3(v)
marks_scored=float(input("Enter the student score in the subject (0-100):"))
#Validate the marks within a plausible range(0-100)
if 0 <= marks_scored <=100:
    if marks_scored >=90:
        grade="A"
        print("grade",grade)
        print("Exellent")
    elif marks_scored >=80:
        grade="B"
        print("grade",grade)
        print("Exellent")
    elif marks_scored >=70:
        grade="C"
        print("Grade",grade)
        print("good")
    elif marks_scored >=60:
        grade="D"
        print("Grade",grade)
        print("satisfactory")

    else:
        grade="F"
        print("Needs imporovement")

