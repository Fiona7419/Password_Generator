from random import *
from Log import pred #user-defined module named Log
from sklearn.preprocessing import LabelEncoder
lbl=LabelEncoder()
n=int(input("Enter number of characters of the password: "))
alpha = [chr(v) for v in range(97, 123)] 
num=[str(i) for i in range(10)]
chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
for i in range(n):
    alpha_num = alpha + num + chars
    pwd = ''.join([choice(alpha_num) for _ in range(n)])
    password=lbl.fit_transform([pwd])
    p=pred(password)
    if(p>0):
        break
print(pwd)



    
    

