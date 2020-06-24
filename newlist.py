#Here \n is used to print the value in next line
#Here \t is used to cerate a space between value
#%s is is use to display the value in order as in box
Name = input("Enter your name: ").lower()
EmployeID = input("Enter your Employee ID: ")
Reason = input("Enter your reason for access: ")
#Open the file
fobj = open("namelist.txt")
text = fobj.read().strip().split()
#Conditions
while True:
    s = Name #Takes input of a string from user
    if s == "": #if no value is entered for the string
        continue
    if s in text: #string in present in the text file
        break
    else: #string is absent in the text file
        print("No such Name found,try again")
        exit()
fobj.close()
if EmployeID.isdigit() :
    print ("Login information: \n\nName:\t%s\nEmployeID:\t%s\nReason:\t%s" % (Name, EmployeID, Reason))
else:
    print("error! type numbers only in employee id section! ")
    exit()

