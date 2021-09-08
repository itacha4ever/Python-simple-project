def game():
    print("Guessing The Number ")

    c_count= 0
    c_limit= 3
    out_of_c= False
    guess=""
    sec_number= "5"

    while guess!= sec_number and not(out_of_c):
        if c_count < c_limit:
            guess = input("Enter Your Guess Number : ")
            c_count+=1
        else:
            out_of_c= True

    if out_of_c:
         print("You lose")

    else:
        print("You Won :D")


game()
