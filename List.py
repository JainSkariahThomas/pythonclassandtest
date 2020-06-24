#Here \n is used to print the value in next line
#Here \t is used to cerate a space between value
#%s is is use to display the value in order as in box
Name = input("Enter your name: ")
EmployeID = input("Enter your Employee ID: ")
Reason = input("Enter your reason for access: ")
if EmployeID.isdigit() :
    print ("Login information: \n\nName:\t%s\nEmployeID:\t%s\nReason:\t%s" % (Name, EmployeID, Reason))
else:
    print("error! type numbers only in employee id section! ")  
    exit()
