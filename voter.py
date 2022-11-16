NAME =    []
DB = {}
B = 0
def vote():
         print(f"candidate list {NAME}")
         IN = input("CAST YOUR VOTE: ").lower()
         DB.update({IN : DB.get(IN)+1})
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
     A =    input("which voter to register: ").lower()
     NAME.append(A)
     print(NAME) 
     DB[A] =    0
     B =    input("do you have more(y/n): ").lower()
     if B == "y":
         B = 0
         create()
     elif B ==    "n":
         vote()
     else:
         print("error")
create()

