def fact(num):
    if( num==0 or num==1) :
        return 1
    else :
        return num*fact(num-1)

number=int(input("Enter the number:"))
print("the factorial of given number is: ",fact(number))


  
