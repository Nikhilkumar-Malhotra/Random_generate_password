import random
password="ABCDEFGHIJLKMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*_-=+<>,.:;'"
length_password=int(input("enter the length of our password:"))
a="" .join(random.sample(password,length_password))
print(f"your password is:12{a}")
