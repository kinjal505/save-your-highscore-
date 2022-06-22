c_score=0
p_score=0
t_score=0
print("you will have to play game for five times and for exit press any number except(0,1,2)")
  
name= input("enter ur name:")
if name.isdigit()==True:
   raise Exception ("enter valid name") 

for i in range(1,6):
   
    import random 
    
    
    user=int(input("enter choice 0:stone,1:paper,2:scissor"))
    if user>=3:
       raise 'please choose between 0,1 or 2, Thank You'
    if user==0: 
      choice='stone'
    elif user==1:
      choice='paper'
    elif user==2:
      choice='scissor'

    comp=random.randint(0,2)
    if comp==0:
      values='stone'
    elif comp==1:
      values='paper'
    elif comp==2:
      values='scissor'
    print(f"your choice:{choice}")
    print(f"comp choice:{values}")

    if(user==comp):
        print("game is tie")
        t_score=t_score+1
        print('no score',t_score)
    elif(user==0 and comp==2 or user==1 and comp==0 or user==2 and comp==1):
      print(f"congratulations you win {name}")
      p_score=p_score+3
    else:
      print("computer wins")
      c_score=c_score+3
		
print(f"comp score is:{c_score}")
print(f"{name} score: {p_score}")
print(f"number of tie:{t_score}")

def score():
    file=open("spc.txt",'r')
    content=file.readlines()
    
    for i in content:
        split=i.split()
        split2=split[2].split()
        file.close()
        if int(p_score) > int(split2[0]):
            f=open('spc.txt','w')
            f.write(f"{name} score: {p_score}")
            print('congratulations {name} high score stored in file')
    file.close()
        
    

score()

    

    


 






