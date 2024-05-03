import random
import string
length=int(input("enter the length of password:"))
print("""set the all types of password like-
      1.Letters
      2.Digits
      3.Special characters
      4.Exit""")
characterList=""
while (True):
    choice=int(input("pick a number"))
    if(choice==1):
        characterList +=string.ascii_letters
    elif(choice==2):
            characterList +=string.digits
    elif(choice==3):
            
            characterList +=string.punctuation
    elif(choice ==4):
             break
             print("please choose a valid option")
password=[]
for i in range(length):
     randomchar = random.choice(characterList)
     password.append(randomchar)
     print("The random password to chossen:" + "".join(password))                       
