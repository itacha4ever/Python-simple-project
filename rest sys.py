import os

def offRestart():
    print("1- For shutdown\n2- for rest\n"
          "Enter any key for exit ")
    choice=input("Enter Your Choice : ")

    if choice=="1":
        os.system("shutdown /s")

    elif choice=="2":
        os.system("restart /r")
    else:
        exit()

offRestart()
