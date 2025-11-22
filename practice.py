marks=float(input("Enter your marks: "))

if marks>=60:
    print("pass")
    if marks>=90:
       print(" your grade is A")
    elif 80<=marks<90:
       print(" your grade is B")
    elif 70<= marks<80:
       print(" your grade is C")
    else:
       print(" your grade is D")
else:
    print("you have failed , study har30""next time")
