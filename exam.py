medicalissue = input("did you have a medical cause? (Y/N):").Strip().upper()

if medicalissue == 'Y':
 print("you are allowd")

else:

    attendance = int(input("enter the attendance of the student:"))

    if attendance >=75:
      print("you are allowed to give exams")
    else:
      print("you are not allowed to give exams")
