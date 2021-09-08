def Login():

    username= "itacha4ever"
    password= "123456"

    input_user= input("enter the user name: ")
    input_password = input("enter the Password: ")

    if input_user == username and input_password == password:
        print("redirecting")
    else:
        print("username or password are wrong  ")

Login()
