a=int(input('enter  first number:'))
b=int(input("enter second number: "))
sum=a+b
difference=a-b
product=a*b
quotient=a/b
flrquotient=a//b
remainder=a%b
power=a**b
print("select an operation")
choice=int(input("Menu:\n"
       "1. Addition\n"
       "2.Subtraction\n"
       "3. Multiplication\n"
       "4. Division\n"
       "5. Floordivision\n"
       "6. Modulus\n"
       "7. exponentiation\n"))
if choice==1:
     print("Sum=",sum)
elif choice==2:
     print("Difference=",difference)
elif choice==3:
     print("Product=",product)
elif choice==4:
     print("Quotient=",quotient)
elif choice==5:
     print("floorQuotient=",flrquotient)
elif choice==6:
     print("Remainder=",remainder)
elif choice==7:
     print("Power=",power)
else:
     print("invalid choice")



