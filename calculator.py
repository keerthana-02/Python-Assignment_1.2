num1=int(input("Enter the value 1: "))
num2=int(input("Enter the value 2: "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponentiation")
choice=int(input("Enter your choice: "))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
elif choice==5:
    print(num1**num2)    
else:
    print("Invalid")
