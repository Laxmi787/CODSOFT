import random
import string

'''upper =string.ascii_uppercase
lowerr =string.ascii_lowercase
digits =string.as
symbols =string.ascii_uppercase
print(upper)'''
U_letters=['a', 'b' ,'c', 'd', 'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
l_letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers= ['0' '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols=['!', '@', '#', '$', '%',  '*', '(' ')', '-', '_', '+'  ]


print("Welcome To Random Password Generator!")
n_uletters=int(input("How many upper case letters you want in your password?\n"))
n_letters=int(input("How many lower case letters you want in your password?\n"))
n_symbols=int(input("How many symbols you want in your password?\n"))
n_numbers=int(input("How many numbers you want in your password?\n"))

password_list=[]
for i in range(1,n_uletters+1):
    char=random.choice(U_letters)
    password_list += char

for i in range(1,n_letters+1):
    char=random.choice(l_letters)
    password_list += char
 

for i in range(1,n_symbols+1):
    char=random.choice(Symbols)
    password_list += char
    
for i in range(1,n_numbers+1):
    char=random.choice(Numbers)
    password_list += char
    
 
random.shuffle(password_list)
 
password=""
for char in password_list:
    password += char
print(password)


print("Process finished with exit code..")