import time

print("Enter your valid username and password")
print("Remember your password is ['abcdef']")
time.sleep(2)

def main():

        username = input("Enter your username:")
        time.sleep(1)
        print("Hai Mr/Mrs.",username)
        time.sleep(1)
        password = input("Enter your password:")

        time.sleep(1)

        if password == "abcdef":
                print("Login Succesfull!")
        else:
            print("Login Failed!")
        time.sleep(2)

        relogin = input("Do You want to login again ? ").lower()

        if relogin == "yes":

                main()
        
        else:
                print("Bye !!!!")
                time.sleep(2)
                quit()

main()        
