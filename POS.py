TAX_RATE = .0625

codeToItem = {
    0 : "Apple",
    1 : "Cake",
    2 : "Toothpaste",
    3 : "Milk"
}

itemToPrice = {
    "Apple" : 1.25,
    "Cake" : 12,
    "Toothpaste" : 3,
    "Milk": 3.75
}

def displayInventory():
    for code, item in codeToItem.items():
        print(str(code)  + ": " + str(item) + " $" +  str(itemToPrice.get(item)))

def printReceipt(order):
    total = 0
    print("Item\tQuantity\tTotal")
    for i in range(len(order)):
        itemPrice = itemToPrice.get(order[i][0])
        itemTotal = itemPrice * order[i][1]
        print(order[i][0] + "\t" +  str(order[i][1]) +  "\t\t$" + str(itemTotal) )
        total += itemTotal
    
    total += total * TAX_RATE
    print("TOTAL: $" + str(total))




import os
def main():
    order = []
    while(True):
        os.system("clear")
        displayInventory()
        code = int(input("Enter the code of the item to add it to your order. Enter -1 to exit"))
        if(code == -1):
            break
        selection = codeToItem.get(code)
        while(True):
            os.system("clear")
            if(code in codeToItem):
                break
            else:
                displayInventory()
                code = int(input("That code was not recognized. Try again."))
                if(code == -1):
                    break
        displayInventory()        
        quantity = int(input("How many?"))
        order.append((selection,quantity))
       
        
    
    printReceipt(order)
        


main()

        
