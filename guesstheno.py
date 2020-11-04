import random 
no = random.randrange(1, 100)
g = 10
print('''WELCOME TO THE GAME 
        GUESS A NUMBER BETWEEN 1 TO 100 ''')

while(g >=0):
    print("No of guess remaining  " + str(g))
    userguess = int(input("Enter your guess \n"))
    ans = str(userguess)
    no = str(no)
    g-=1
    if ans == no :
        print("Your guess is right !!!\n")
        print("No of guess took to win :  "+str(10-g))
        break

    elif str(g) == '0' :
        print("GAME OVER !!!")
        print("The correct no was :- "+str(no))
        break
    elif ans > no :
        print("Take a smaller guess !!!")
        continue
    elif ans < no :
        print("Take a Bigger guess !!!")
        continue
