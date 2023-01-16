from random import *
import time


def Clear():
    for i in range(0,100):
        print("\n") #this to clear console because i didnt find humane way

class Password:

    def __init__(self):
        self.password =  self.confirm_pass(self.check_pass_req(self.get_pass())) #not sure what this is

    def encrypt(self, password): #forgot what this is
        key = randint(1, 100)
        encrypted = ""
        for i in password:
            if i ==" ":
                encrypted+=" "
            elif (i.isdigit()):
                encrypted += i
            elif (i.isupper() and i.isdigit()==False):
                encrypted += chr((ord(i) + key - 65) % 26 + 65)
            else:
                encrypted += chr((ord(i) + key - 97) % 26 + 97)

        print(f"Original Password: {password}\nShift Value: {key}\nEncrypted Pass: {encrypted}")


    def confirm_pass(self, password): #idk somethign to do with password
        global done
        attempts = 0
        while(self.password!=str(input("Confirm Password: "))):
            attempts+=1
            if(attempts>2):
                break
        if(attempts==3):
            print("Too Many Attempts!!")
            time.sleep(1)
            print("Restarting")
            time.sleep(2)
            Clear()
            Password()

        if(attempts<3):
            print("Starting TO Encrtpt")
            self.encrypt(self.password)


        return password

    def check_pass_req(self,password): #check for reqouns or smthing idk
        Flag = False
        if(len(password)<4):
            print("Couldn't even write a long enough password..")
            Flag = True
        if (any(not c.isalnum() for c in password)) == True:
            print("Can you please not include weird characters.. i want to throw up..")
            Flag = True

        if(any(c.isupper() for c in password) == False or any(d.isdigit() for d in password) == False):
            print("YU MUST HAVE ATLEAST 1 digit and 1 capitalized letter")
            Flag = True


        if(Flag==True):
            self.check_pass_req(self.get_pass())

        return password

    def get_pass(self): #get password
        self.password = str(input("Password: "))
        return self.password

UserCypherdPass = Password()
