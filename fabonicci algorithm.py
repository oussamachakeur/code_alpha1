def Fibonacci (n):
    a , b = 0,1
    print ('your Fibonacci  serie will be : ')
    for x in range (n):
        s= a+ b 
        b = a
        a = s 
        print(s, end=' ')
n= int(input("please enter the numbers u want from fabonicci sequence: "))
if n<=0 :
    print("please enter a positive integer ")
else :    
    Fibonacci (n)
