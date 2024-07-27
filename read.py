def start():
     # Function to display the header of the Laptop Pasal store.

     # Display header with store name and contact information.
    print("\n")
    print("*************************************************************************************************************************************")
    print("\t \t \t \t \t \t \t \t \t   Laptop Pasal")
    print("\n")
    print("\t \t \t \t \t \t \t \t  Nepal , kathmandu   -  9841414141")
    print("*************************************************************************************************************************************")
    print("\n")

def XYZ():
    # Function to read the laptops data from a text file and return it as a dictionary.
    
    #initialize an empty dictionary to store.
    dictonary = {}
    file = open("laptops.txt", "r")
    laptopid = 1
     # Read each line of the file and store it in the dictionary.
    for i in file:
        i = i.replace("\n", "")
        dictonary.update({laptopid : i.split(",")})
        laptopid += 1
    file.close()

    return dictonary

def display():
    #to display data
    a=1
    """This function help to show laptops details in a table."""
    text= open("laptops.txt","r")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("SN"'\t\t',"Name"'\t\t\t\t',"Brand"'\t\t\t',"price"'\t\t\t',"Quantity Aviable",'\t'"Processor"'\t',"Graphic Card")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    for value in text:
        print(a, "\t\t"+value.replace(",","\t\t"))
        a= a+1
    return value