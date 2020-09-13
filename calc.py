print("Welcome to the calculator \n")


no1 = int(input("Enter first no :- "))
no2 = int(input("Enter second no:- "))
op = input('''choose an operator :-     '+'  For Addition
                                        '-'  For Substraction
                                        '*'  For Multiplication 
                                        '/'  For Division 
                                         Enter the opertator :-  ''')


# checking what is the operator and printing the result 
 
if op=='+':
    print(no1+no2)
elif op=='-':
    if no1>no2:
        print(no1-no2)
    else: 
        print(no2-no1)
elif op=='/':
    print(no1/no2)
    
else:
 print(no1*no2)


print("Thanks for using this calculator :>")
