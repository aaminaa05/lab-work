#ex1
import os 
path=input("Write path: ")
dir_list=os.listdir(path)
print("Directories: ")
for dir in dir_list:
    print(dir)
print("\nFiles: ")
for dir in dir_list:
    if os.path.isfile(dir):
        print(dir)

#ex2
import os

path=input("Enter path: ")
print("exist: ",os.access(path, os.F_OK)) #existance
print("readable: ",os.access(path, os.R_OK)) #readable
print("writable: ",os.access(path, os.W_OK)) #writability
print("exucutable: ",os.access(path,os.X_OK)) #exucutable

#ex3
import os

path=input("Enter path: ")
if os.access(path,os.F_OK):
    print("given path exists")
    print("filename: ",os.path.basename(path))
    print("dirname: ",os.path.dirname(path))
else:
    print("does not exists")

#ex4
cnt=0
with open("text_forex4.txt","r") as file:
    for i in file:
        cnt+=1
print(cnt)

#ex5
with open("text_forex5.txt","w") as file:
    mylist=[]
    n=input("Enter numbers: ")
    for i in n.split():
        num=int(i)
        mylist.append(num)
    print(mylist)
    file.write(str(mylist))

#ex6
import string
for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as file:
        file.write(letter + "\n")

#ex7
with open("copy1.txt","r") as copy1, open("copy2.txt", "w") as copy2:
    for i in copy1:
        copy2.write(i)

#ex8
import os

path = input("Enter path: ")
if os.path.exists(path):
    print("given path exists")
    if os.path.isfile(path):
        os.remove(path)
        print("file wad deleted")
    elif os.path.isdir(path):
        os.rmdir(path)
        print("dir  was deleted")
else:
    print("does not exists")

#BUILTIN
#ex1
n=input("Enter numbers: ")
mylist=[]
for i in n.split():
    num=int(i)
    mylist.append(num)
x=iter(mylist)
multiply=1
for i in mylist:
    multiply*=next(x)
print(multiply)

#ex2
str1=input("Enter your string: ")
up_l=0
lw_l=0
for i in str1:
    if i.isupper():
        up_l+=1
    if i.islower():
        lw_l+=1
print("The number of upcase letters: ",up_l, "\n", "The number of lowcase letters: ",lw_l)

#ex3
str1=input("Enter your string: ")
if str1 == str1[::-1]:
    print("Yes")
else:
    print("No")

#ex4
from math import sqrt
from time import sleep
n=int(input("Enter number: "))
t=int(input("Enter milliseconds: "))
sleep(t/1000)
print("Square root of ",n, "after ",t,"miliseconds is ",sqrt(n))

#ex5
n = input("Enter elems: ")
mytuple = tuple(bool(int(elem)) for elem in n.split())
print(all(mytuple))



