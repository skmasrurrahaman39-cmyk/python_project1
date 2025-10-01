names = input("Enter your name: ")

if(names.startswith("s")):
    print(f"sir {names}")
elif(names.startswith("m")):
    print(f"madam {names}")
else:
    print(f"sir/madam {names}")

def calculator():
    name = f"sir {names}" if(names.startswith("s"))  else f"sir/madam {names}"

    age = input("Enter your age: ")

    print(f"----Welcome {name} ----")
    use_cl = 0
            
    while True:
        user = int(input("Enter your choice\n1 for +\n2 for -\n3 for x\n4 for /\n5 for exit & close\n--->"))
            
        if user == 1:
            num1 = int(input("you choised +\nEnter first number: "))
            num2 = int(input(f"{num1} + "))
            result = num1 + num2
            print(f"<<< {name} restlt is = {result} >>>")
            use_cl += 1


            
        elif user == 2:
            num1 = int(input("you choised -\nEnter first number: "))
            num2 = int(input(f"{num1} - "))
            result = num1 - num2
            print(f"<<< {name} restlt is = {result} >>>")
            use_cl += 1

            
        elif user == 3:
            num1 = int(input("you choised x\nEnter first number: "))
            num2 = int(input(f"{num1} x "))
            result = num1 * num2
            print(f"<<< {name} restlt is = {result} >>>")
            use_cl += 1

            
        elif user == 4:
            num1 = int(input("you choised /\nEnter first number: "))
            num2 = int(input(f"{num1} / "))
            result = num1 // num2
            print(f"<<< {name} restlt is = {result} >>>")
            use_cl += 1


        elif user == 5:
            print(f"{name()} age {age} You used calculator {use_cl} times.")
            print("program has been cloaed....")
            break


        else:
            print("!!! Error, you choise invalid number !!! ")

            

calculator()