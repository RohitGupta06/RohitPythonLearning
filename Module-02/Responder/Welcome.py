# Welcoming The User

# Initializing Variable
Welcome_message = Lastname = Firstname = Gender = Name = Wait_message = " "

# Welcome Message
Welcome_message = "Good Morning!, Welcome to Medha Innovation and Development Private Limited."

# Displaying the Welcome Message
print(Welcome_message)

# Taking Users Info
Lastname = input("May I know your Last Name? ")
Firstname = input("May I know your First Name? ")
Gender = input("May I know your Gender? ")

if(Gender == 'Male' or Gender == 'male'):
    Name = input("Whom do you want to meet Sir? ")
elif(Gender == 'Female' or Gender == 'female'):
    Name = input("Whom do you want to meet Ma'am? ")

# Wait Message
Wait_message = "Mr. {} will be meeting you in 10mins meanwhile I request to have a seat and enjoy a cup of coffee :)".format(Name) 

# Displaying the Wait Message
print(Wait_message)       