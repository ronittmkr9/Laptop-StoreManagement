import read


def updatesell(lap_id, noOfLaptops, list):
    
    file = read.XYZ()
    for i in file.keys():
        if lap_id == i:
            quantity = int(file[lap_id][3])
            if noOfLaptops <= quantity:
                file[lap_id][3] = str(quantity - noOfLaptops)  # quantity update in dectonary
                price = noOfLaptops * int(file[lap_id][2].replace("$", ""))
                list.append([file[lap_id][0], file[lap_id][1], file[lap_id][2], price, noOfLaptops])

    return file


def updatepurchase(lap_id, laptopQuantity, list):
    
    file = read.XYZ()
    for i in file.keys():
        if lap_id == i :
            quantity = int(file[lap_id][3])
            print(quantity + laptopQuantity)
            file[lap_id][3] = str(quantity + laptopQuantity)  

            price = laptopQuantity * int(file[lap_id][2].replace("$", ""))
            list.append([file[lap_id][0], file[lap_id][1], file[lap_id][2], price, laptopQuantity])
    return file


def check(dict):
    check_loop = True
    value = list(dict.keys())
    earl = value[-1]
    while check_loop:
        try:
            lap_id = int(input("Enter The Laptop ID: "))
        except ValueError as num:
            print("please enter option correctly.")
            break
        else:
            if lap_id <= 0:
                print("please enter in valid format ")
            elif 0 <= lap_id <= earl:
                check_loop = False
            else:
                print("please enter in valid format")
    return lap_id

def check_quantity1(dict, lap_id, input_user):
    check_loop = True
    while check_loop: 
        try:
            quantity_laptop1 = int(input("Enter the quantity of laptops you want to sell: "))
        except ValueError as num:
             print("please enter in valid format")
        else:
            avaiable = int(dict[lap_id][3])
            if input_user == 1:
                if avaiable >= quantity_laptop1:
                    check_loop = False
                else:
                    check_loop = False
            elif input_user == 2:
                if quantity_laptop1 <= 0:
                    print("Quantity shouldn't be in negative")
                else:
                    check_loop = False
    return quantity_laptop1

def check_quantity(dict, lap_id, input_user):
    
    check_loop = True
    while check_loop: 
        try:
            quantity_laptop = int(input("Enter the quantity of laptops you want to buy: "))
        except ValueError as num:
            print("please enter in valid Format")
        else:
            avaiable = int(dict[lap_id][3])
            if input_user == 1:
                if avaiable >= quantity_laptop:
                    check_loop = False
                else:
                    print("There is only ",avaiable, "left. ")
            elif input_user == 2:
                if quantity_laptop <= 0:
                    print("Quantity shouldn't be in negative")
                else:
                    check_loop = False
    return quantity_laptop
