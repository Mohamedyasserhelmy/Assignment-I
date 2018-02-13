
a=[0,1,2,3,4,5,6,7,8] # declaring an array to put X or O
import os
os.system('cls')
import time # time function to quit the game
counter=1 # alternating between Player 1 and Player 2     

# printing the game board
def main():
    print('X-O GAME    PLAYER 1~~~X    PLAYER 2~~~O')
    print('_________\n')
    print(a[0], '|' ,a[1], '|',a[2])
    print('_________\n')
    print(a[3], '|' ,a[4], '|',a[5])
    print('_________\n')
    print(a[6], '|' ,a[7], '|',a[8]) 
                 
# the main loop of the game            
while True:
    
    print(main())
    i=int(input("Choose a place to play: "))
    print("_________\n")

    if a[i]!='x' and a[i]!='o':
        
        if counter%2==1 :
                a[i]='x'
                
        if counter%2==0 :
            a[i]='o'
    else:
        print("this place is taken!!")
        counter=counter-1
        time.sleep(1)

# winning conditions for x
    if(a[0]=='x' and a[3]=='x' and a[6]=='x')\
    or(a[1]=='x' and a[4]=='x' and a[7]=='x')\
    or(a[2]=='x' and a[5]=='x' and a[8]=='x')\
    or(a[0]=='x' and a[1]=='x' and a[2]=='x')\
    or(a[3]=='x' and a[4]=='x' and a[5]=='x')\
    or(a[6]=='x' and a[7]=='x' and a[8]=='x')\
    or(a[2]=='x' and a[4]=='x' and a[6]=='x')\
    or(a[0]=='x' and a[4]=='x' and a[8]=='x'):
        print(main())
        print("~~~X WINS~~~")
        time.sleep(5)
        break
# winning conditions for o
    if(a[0]=='o' and a[3]=='o' and a[6]=='o')\
    or(a[1]=='o' and a[4]=='o' and a[7]=='o')\
    or(a[2]=='o' and a[5]=='o' and a[8]=='o')\
    or(a[0]=='o' and a[1]=='o' and a[2]=='o')\
    or(a[3]=='o' and a[4]=='o' and a[5]=='o')\
    or(a[6]=='o' and a[7]=='o' and a[8]=='o')\
    or(a[2]=='o' and a[4]=='o' and a[6]=='o')\
    or(a[0]=='o' and a[4]=='o' and a[8]=='o'):
        print(main())
        print("~~~O WINS~~~")
        time.sleep(5)
        break
# draw condition
    elif counter==9:
        print(main())
        print("~~~~Draw~~~~~")
        time.sleep(5)
        break
    counter+=1

    


#All copyrights reserved






















    
