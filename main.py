#Author: Jason Vanderhoff jkv5212@psu.edu

acc = 0;
totCred = 0;
def letter_grade(grade):
  if(grade == "A"):
    return 4

  elif(grade == "A-"):
    return 3.67

  elif(grade == "B+"):
    return 3.33

  elif(grade == "B"):
    return 3

  elif(grade == "B-"):
    return 2.67

  elif(grade == "C+"):
    return 2.33

  elif(grade == "C"):
    return 2

  elif(grade == "D"):
    return 1

  else:
    return 0


for x in range(1, 4):
  letter = input(f"Enter your course {x} letter grade: ")
  cred = input(f"Enter your course {x} credit: ")
  totCred = totCred + float(cred)
  lGrade = letter_grade(letter)
  acc = acc + lGrade * float(cred)
  print(f"Grade point for course {x} is: {float(lGrade)}")

print(f"Your GPA is: {acc/totCred}")

