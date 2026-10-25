#  Project 1 ATM Simulator
balance = 10000
correct_pin = 1234
attempt = 1
print("Choice option:")
print("1.Balances","2.Deposit")
print("3.Withdraw","4.Exit")
while attempt<=3:
    pin = int(input("enter the pin:"))
    if correct_pin == pin:
        while True:
            balances = 1
            deposit = 2
            withdraw = 3
            exit = 4
            option = int(input("enter the option:"))
            if option == balances:
                    print(balance)
            elif option == deposit:
                depo=int(input("enter the deposit amount:"))
                if depo > 0:
                    balance = balance + depo
                print("Deposit succesfully:",depo)
                print("Total Balance:",balance)
                
            elif option == withdraw:
                wit_draw = int(input("enter the withdraw amount:"))
                if wit_draw <= balance:
                    print(f"Withdraw succesfully:{wit_draw} ")
                    print("Left Balance:",balance-wit_draw)
                else:
                    print("Insufficient value")
            elif option == exit:
                print("Thank you")
                
                break
        break       
    elif attempt<=3:
        print("left attempt",3-attempt)
        attempt+=1
        if attempt == 4:
            print("Card blocked")
            break
      
#  project 2 Marks Manager
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
print("Choice option-")
print("1. Add students")
print("2. View all")
print("3. Show topper")
print("4. Exit")
  
while True:

    option = int(input("Enter the option:"))

    if option == 1:
        key = input("enter the key:")
        for name in students:
              if key == name:
                     print("Already exit key")
                     break
              
                     
        count = 0
        values = []
        while count<3:
               a = int(input("Enter the value:"))
               if 0<a<=100:
                     values.append(a)
               count+=1     
               students[key] = values
               print("Added Succesfully")
    elif option == 2:
        for name in students:
            avg = sum(students[name])/3
            if avg>=85:
                     grade = "A"
            elif 70<=avg<85:
                     grade = "B"
            elif 50<=avg<70:
                     grade = "C"
            else:
                     grade = "F"
            print(name, round(avg, 2),grade)
    elif option == 3:
           topper = ""      
           highest = 0
           for name in students:
                  avg = sum(students[name]) / 3
                  if avg > highest:
                         
                         highest = avg
                         topper = name
           print("Topper:",topper)
    elif option ==4:
           print("Goodbye!")
     
           break 
    else:
           print("Invalid option , choose 1 to 4.")  
          
            

        
