#Display Menu
print("Menu")
print("G: Gas")
print("O: Oil")

#Ask for User Input
userInput = input("Select an option (G or O): ").upper()
#User input is G
if userInput == 'G':
    gasLitres = int(input("Enter the number of litres of gas: "))
    totalCost = gasLitres * 1.07
# discount if gaslitres more than 4000
    if gasLitres > 4000:
        totalCost *= 0.9  
# Ask for province 
    province = input("Enter the province: ").upper()

    if province in ["AB", "BC", "MB", "NT", "NU", "QC", "SK", "YT"]:
        gst_percent = 5
    elif province == "ON":
        gst_percent = 13
    else:
        gst_percent = 15
# Calulate the GST amount and then total Cost
    gst_amount = (totalCost * gst_percent) / 100
    totalCost += gst_amount
# Output
    print(f"Total cost for gas: ${totalCost:.2f}")
# If user input is O
elif userInput == 'O':
    oilCases = int(input("Enter the number of cases : "))
    totalLitres = oilCases * 12
    totalCost = oilCases * 12 * 1.27
# Discount applies if more than 8 cases chosen
    if oilCases > 8:
        totalCost *= 0.9
# Ask for province
    province = input("Enter the province: ").upper()

    if province in ["AB", "BC", "MB", "NT", "NU", "QC", "SK", "YT"]:
        gst_percent = 5
    elif province == "ON":
        gst_percent = 13
    else:
        gst_percent = 15
# Calculate the GST amount and total cost
    gst_amount = (totalCost * gst_percent) / 100
    totalCost += gst_amount
# Output
    print(f"Total cost for oil: ${totalCost:.2f}")
# Invalid output if output is not O and G.
else:
    print("Invalid input, you should enter G or O.")

