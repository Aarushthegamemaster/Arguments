import os
options = str(input("Do you want to shut down your computer:"))

if options == "Yes" or "yes" or "Yeah" or "yeah" or "Yup" or "yup":
    os.system("shutdown /s /t 0")
elif options == "no" or "No":
    print("Ok, you can close the program now!")
else:
    print("Invalid input! Please try again")