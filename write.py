import read
def textupdate(dictionary):
    file=open("laptops.txt","w")
    for i in dictionary.values():
        file.write(str(i[0])+","+ str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5]))
        file.write("\n")
    file.close()

def billSold(name,number,list,bill_num,date_today,time):
    global shipping #Declare a global variable
    shipping = input("Do you want us to deliver it?(y/n)")
    ship= True
    while ship:
        if shipping.lower() == "y":
            ship=False
            
        elif shipping.lower() == "n":
            ship = False
        else:
            print("Please Choose option Correctly")
    read.start()
    print(f"Bill no: {bill_num}")
    print(f"date: {date_today}\t\t Time: {time}")
    print("-------------------------------------------------------------------------")
    print(f"Name:  {name}")
    print(f"Number: {number}")
    final=0

# Iterate through each item in the list of purchased items
    for i in range(len(list)):
        Brand_name=list[i][1].replace(" ","")
        print(f"Name: {list[i][0]}\t\tBrand: {Brand_name}") 
        price1 =list[i][2].replace(" ","")
        print(f"Price: {price1}\t\t\t Quantity: {list[i][4]}")
        print(f"Total price: {list[i][3]}")
        final=final+int(list[i][3])
        print(f"\n")
    if shipping=="y":
        print(f"Delivery Charge: {250}")
        print(f"Total without Delivery Charge: {final}")
        print(f"Total: {final+250}")
    else:
        print(f"Total: {final}")

#bill
def text_billsold(name,num,list,bill_no,date,time):
    file = open(f"{bill_no}.txt","w")
    file.write(f"/t/t/tBill no: {bill_no}\n")# write the bill number to the file
    file.write(f"date: {date}\t\t\t\t\t Time: {time}\n")#date
    file.write(f"name:  {name}\n")
    file.write(f"Number: {num}\n")
    final=0
 # loop through list of purchased laptops and write its details to the file
    for i in range(len(list)):
        Brand_name=list[i][1].replace(" ","")
        file.write(f"Laptop Name: {list[i][0]}\t\t\tBrand: {Brand_name}\n")
        price1 =list[i][2].replace(" ","")
        file.write(f"Price: {price1}\t\t\t\t\t Quantity: {list[i][4]}\n")
        file.write(f"Total price: {list[i][3]}\n")
        final=final+int(list[i][3])
        file.write(f"\n")
    if shipping=="y":
        file.write(f"Delivery Charge : {250}\n")
        file.write(f"Total without Vat: {final}\n")
        file.write(f"Total: {final+250}\n")
    else:
        file.write(f"Total: {final}\n")

#Bill
def billBuy(name,list,bill_no,date,time):

    read.start()

    print(f"Bill no: {bill_no}")
    print(f"Date: {date}\t\t Time: {time}")
    print("-------------------------------------------------------------------------")
    print(f"Name:  {name}")
    total=0


    for i in range(len(list)):
        Brand_name=list[i][1].replace(" ","")
        print(f"Laptop Name: {list[i][0]}\t\tCompany Name: {Brand_name}") 
        price1 =list[i][2].replace(" ","")
        print(f"Price: {price1}\t\t \nQuantity: {list[i][4]}")
        print(f"Total price: {list[i][3]}")
        total=total+int(list[i][3])
        print(f"\n")
#Extraxts Total amt and total vat amt
    print(f"Total Vat amount: {0.13*total}")
    print(f"Total With Vat :{(0.13*total) + total}")

# This function generates a bill for a laptop purchase.
# The bill is written to a text file with the given bill number.
def textbill_Buy(name,list,bill_no,date,time):
    file = open(f"{bill_no}.txt","w")
    file.write(f"Bill no: {bill_no}\n")
    file.write(f"Date: {date}\t\t Time: {time}\n")
    file.write(f"Name:  {name}\n")
    total=0

    for i in range(len(list)):
        Brand_name=list[i][1].replace(" ","")
        file.write(f"Laptop Name: {list[i][0]}\t\t\tBrand: {Brand_name}\n")
        price1 =list[i][2].replace(" ","")
        file.write(f"Price: {price1}\t\t\t\t\t \nQuantity: {list[i][4]}\n")
        file.write(f"Total price: {list[i][3]}\n")
        total=total+int(list[i][3])
        file.write(f"\n")
    file.write(f"Total Vat : {0.13*total}\n")
    file.write(f"Total with VAT = {(0.13*total) + total}\n")