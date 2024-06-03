import random
num_list=['0','1','2','3','4','5','6','7','8','9']
letter_list=['a','b','c','d','e','f','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B',
             'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol_list=['!','#','$','@','%','^','&','*','(',')','+']
print("welcome to password generator!")
print(input("How many numbers you want in your password?"))
n_number=random.randint(0,9)
print(n_number)
print(input("How many letters would you like?"))
n_letter=random.randint(0,9)
print(n_letter)
print(input("How many symbols would you like?"))
n_symbol=random.randint(0,9)
print(n_symbol)
password_list=[]
for i in range(0,n_number):
    char=random.choice(num_list)
    password_list+=char
for j in range(0,n_letter):
    char=random.choice(letter_list)
    password_list+=char
for k in range(0,n_symbol):
    char=random.choice(symbol_list)
    password_list+=char
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for i in password_list:
    password+=i
print(password)