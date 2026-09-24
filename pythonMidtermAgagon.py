print("=========================================")
print("      Sales Record Management System")
print("=========================================")
print("1. Add Sale Record")
print("2. View All Records & Summary Statistics")
print("3. Clear All Sales Data")
print("4. Exit System")
print("=========================================")

option = int(input("Enter the number of option you would like to do : "))

# Option 1
if option == 1:

    item = input("Enter item name: ")
    quantity = int(input("Enter quantity sold: "))
    pricePerUnit = float(input("Enter the price per unit: "))
    totalAmount = quantity * pricePerUnit

    file = open("sales_log.txt", "a")
    file.write(f"{item},{quantity},{pricePerUnit},{totalAmount}\n")
    file.close()

    print()
    print("Item name: " + item)
    print(f"Quantity: {quantity}")
    print(f"Price per unit: {pricePerUnit:.2f}")
    print(f"Total amount: {totalAmount:.2f}")
    print("Sale record saved successfully.")


# Option 2
elif option == 2:

    try:
        file = open("sales_log.txt", "r")

        lines = file.readlines()
        file.close()

        if len(lines) == 0:
            print("No records found.")

        else:
            totalUnitsSold = 0
            grandTotalRevenue = 0.0

            for line in lines:

                data = line.strip().split(",")
                item = data[0]
                quantity = int(data[1])
                pricePerUnit = float(data[2])
                totalAmount = float(data[3])

                print(f"Item Name: {item}")
                print(f"Quantity Sold: {quantity}")
                print(f"Price Per Unit: {pricePerUnit:.2f}")
                print(f"Total Amount: {totalAmount:.2f}")

            print(f"Total Units Sold: {totalUnitsSold}")
            print(f"Grand Total Revenue: {grandTotalRevenue:.2f}")

    except FileNotFoundError:
        print("No records found.")


# Option 3
elif option == 3:
    file = open("sales_log.txt", "w")
    file.close()

    print("All records cleared. No records remaining.")


# Option 4
elif option == 4:
    print("Thank you for using the Sales Record Management System")
    exit()