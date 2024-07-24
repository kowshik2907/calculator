print("CALCULATOR")
i=0
while i==0:
    val_1=int(input("Enter First value :"))
    val_2=int(input("Enter Second Value :"))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice=int(input("Enter Operation :"))
    if choice==1:
        print("Addition of Values is:",val_1+val_2)
    elif choice==2:
        print("Subtraction of Values is:",val_1-val_2)
    elif choice==3:
        print("Multiplication of Values is:",val_1*val_2)
    elif choice==4:
        print("Division of Values is:",val_1/val_2)
    elif choice==5:
        i+=1
    else:
        print("Enter a valid Operation")