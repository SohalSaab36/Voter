import os
import time
def touch(path):
    with open(path, 'w'):
        os.write(DB)
#print(os.getcwd())
#print(os.listdir())
sec =    time.time()
lat =    time.ctime(sec).upper()
root =    os.getcwd()
check =   os.path.exists(f"{root}/log")
#print(check)
if check ==    True:
    os.chdir(f"{root}/log")
else:
    os.mkdir(f"{root}/log")
    os.chdir(f"{root}/log")
#print(os.getcwd())
#print(os.listdir())
lt =    ''.join(lat.split())
log =    open(f"{lt}.txt",'w')
NAME =    []
DB = {}
B = 0
print(lt)
def vote():
         
         print(f"candidate list {NAME}")
         IN = input("CAST YOUR VOTE: ").lower()
         
         if IN in DB:
             DB.update({IN : DB.get(IN)+1})
         else:
             vote()
             
         ASK =    input("more voters ?(y/n) :    ").lower()
         if ASK ==    "y":
             vote()
         elif ASK ==    "n":
             
             exit()
         elif ASK ==    "key":
             print(DB)
         else:
             vote()
 
def create():
     A =    input("which voter to register: ")
     NAME.append(A)
     print(NAME) 
     DB[A] =    0
     B =    input("do you have more(y/n): ")
     if B == "y":
         B = 0
         create()
     elif B ==    "n":
         vote()
     else:
         print("error")
create()
