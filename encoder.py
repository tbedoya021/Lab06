def encoder(password):
    list(password)
    for digit in range(len(password)):
        if password[digit] == "1":
            password[digit] = '4'
        elif password[digit] == "2":
            password[digit] = '5'
        elif password[digit] == "3":
            password[digit] = '6'
        elif password[digit] == "4":
            password[digit] = "7"
        elif password[digit] == "5":
            password[digit] = "8"
        elif password[digit] == "6":
            password[digit] = "9"
        elif password[digit] == "7":
            password[digit] = "0"
        elif password[digit] == "8":
            password[digit] = "1"
        elif password[digit] == "9":
            password[digit] = "2"
        elif password[digit] == "0":
            password[digit] = "3"
        password_str = ""
        for i in password:
            password_str += str(i)
    return password_str






def main():
    while True:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")
        selection = input("Please enter an option: ")
        if selection == '1':
            password = list(input("Please enter your password to encode: "))
            encoder_str = encoder(password)
            print("Your password has been encoded and stored! \n")
        elif selection == '2':
            pass
        elif selection == '3':
            quit()



if __name__ == "__main__":
    main()


