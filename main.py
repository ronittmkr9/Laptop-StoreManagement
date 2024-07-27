

import read
import write
import operation
import datetime
import random
def heading():
    print("\n")
    print("\n")
    print("*******************************************************************************************************************************************")
    print("\t \t \t \t\t\t\t\t LapTop Pasal")#Tab space
    print("\n")
    print("\t \t \t \t\t\t\t","    Nepal,Kathmandu  - 9841414141")#Tab space
    print("\n")
    print("*******************************************************************************************************************************************")
    print("\t \t \t\t\t\t\t","   Welcome To Laptop Pasal")
    print("*******************************************************************************************************************************************")
    print("\n")
heading()

def main():
    
    boolean = True
    while boolean == True:
        print("Enter your option")
        print("Enter 0 to Show List of laptops")
        print("Enter 1 to Sell")
        print("Enter 2 to Buy")
        print("Enter 3 to Exit")
        b2 = True
        while b2:
            try:
                inputuser = int(input("Enter the option to Continue: "))
            except ValueError:
                print("Enter from option")
            else:
                b2 = False
        print("\n")





        if inputuser == 0:
            read.display()
            print("Thankyou")
        elif inputuser == 2:
            read.display()
            print("*************************************************************************************************************************************")
            boolean = True
            loop = True
            while loop:
                user_name = str(input("Enter your Name : "))
                try:
                    if user_name.isalpha():
                        break
                    else:
                        raise ValueError("INVALID INPUT")
                except ValueError as cde:
                    print(f"error:{cde}")
                else:
                    loop = False
            
            loop_Num = True
            while loop_Num:
                try:
                    num = int(input("Enter your contact number: "))
                except ValueError:
                    print("Enter in valid Form")
                else:
                    loop_Num= False

            list = []
            boolean_3 = True
            while boolean_3:
                b3 = True
                dict = read.XYZ()
                while b3:
                    lap_id = operation.check(dict)
                    if int(dict[lap_id][3]) == 0:
                        operation.loop(b3)
                    else:
                        b3 = False
                    laptop_left = operation.check_quantity(dict, lap_id, inputuser)
                    dict = operation.updatesell(lap_id, laptop_left, list)
                    write.textupdate(dict)
                    loop_4 = True
                    while loop_4:
                        ask_again = str(input("Do you want to buy again :(y/n) "))
                        if ask_again == 'y':
                            loop_4 = False
                            boolean_3 = True
                        elif ask_again == 'n':
                            loop_4 = False
                            boolean_3 = False
                        else:
                            print("Please enter appropriate value")
                            boolean_3 = False
                            break
            bill_number1 = random.randint(0, 100)
            date_now1 = datetime.datetime.now().strftime("%d/%m/%Y")
            time_now1 = datetime.datetime.now().strftime("%H:%M:%S")
            write.billSold(user_name, num, list, bill_number1, date_now1, time_now1)
            write.text_billsold(user_name, num, list, bill_number1, date_now1, time_now1)
            print("\n")
            print("Thankyou")
        elif inputuser == 1:
            read.display()
            print("****************************************************************************************************************************************************")
            try_loop = True
            while try_loop:
                user_name = input("Enter you Name: ")
                try:
                    if user_name.isalpha():
                        break
                    else:
                        raise ValueError("INVALID INPUT")
                        
                except ValueError as cde:
                    print(f"error:{cde}")
                else:
                    try_loop = False
                    
            dictionary = read.XYZ()
            list = []
            boolean_2 = True
            while boolean_2 == True:
                lap_id = operation.check(dictionary)
                    
                if   int(dictionary[lap_id][3]) == 0:
                        operation.loop(b3)
                else: 
                        b3 = False
                
                quantity_left = operation.check_quantity1(dictionary, lap_id, inputuser)
                dictionary = operation.updatepurchase(lap_id, quantity_left, list)
                write.textupdate(dictionary)
                loop_Buy = True
                while loop_Buy:
                    ask_again = str(input("Do you want to sell again : "))

                    print("*******************************************************************************************************************************************")
                    if ask_again == 'y':
                        loop_Buy= False
                        boolean_2 = True
                    elif ask_again == 'n':
                        loop_Buy = False
                        boolean_2= False
                    else:
                        boolean_2 = False
                        print("Please enter appropriate value")
            bill_number = random.randint(0, 500)
            date_now = datetime.datetime.now().strftime("%d/%m/%Y")
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            write.billBuy(user_name, list, bill_number, date_now, time_now)
            write.textbill_Buy(user_name, list, bill_number, date_now, time_now)
            print("\n")
            print("Thankyou.")
        elif inputuser == 3:
            boolean = False
            print("Thankyou")
            print("\n")
        else:
            print("The option you entered do not matched tho option in our system")
            print("\n")
    return inputuser
main()

