import string as str
import random as ran

char=list(str.ascii_uppercase+str.ascii_lowercase+str.digits+"$!$#^&")
# print(char)
def passwd():
    n=int(input('enter no of  password count you needed?'))

    l=[]
    for i in range(n):
        l.append(ran.choice(char))
    
    
    print(l)  
    
    print(''.join(l)) 
    
     
        

password=passwd()
