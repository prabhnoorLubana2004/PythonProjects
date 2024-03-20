'''Calculating the mortgage. Code is divided into two sections. '''
client_name=input("Enter  client name=")
client_address=input("Enter address of property=")
purchase_price=float(input("Enter purchase price="))

if(purchase_price<=500000):
    cal=purchase_price*(5/100)
    down_percentage_min=(cal/purchase_price)*100
    down_percentage_min=float(down_percentage_min)
    down_percentage_min_round=round(down_percentage_min,3)
 
elif(purchase_price>500000 and purchase_price<1000000):
    cal=500000*(5/100)+((purchase_price-500000)*(10/100))
    down_percentage_min=(cal/purchase_price)*100
    down_percentage_min_round=round(down_percentage_min,3)
else:
#if purchase price is more 
     cal=purchase_price*(20/100)
     down_percentage_min=(cal/purchase_price)*100
     down_percentage_min_round=round(down_percentage_min,3)
#Now, we will ask the user to enter the down payment percentage.
down_payment_percentage=float(input(f'Enter down payment percentage(minimum{down_percentage_min_round}%)-'))
#if down payment percentage is less than minimum down percentage required.
while(down_payment_percentage<down_percentage_min_round or down_payment_percentage>100):
    print(f'Please enter a value between the minimum {down_percentage_min_round} and 100')
    down_payment_percentage=float(input(f'Enter down payment percentage(minimum {down_percentage_min_round}%)-'))
#After user enter the correct down payment percentage.
if(down_payment_percentage>=5 and down_payment_percentage<10):
    insurance_rate=4
elif(down_payment_percentage>=10 and down_payment_percentage<15):
    insurance_rate=3.1
elif(down_payment_percentage>=15 and down_payment_percentage<20):
    insurance_rate=2.8
else:
    insurance_rate=0
    print("Insurance is not required")
#After the insurance rate, we will calculate the down payment amount, Insurance cost and total mortage amount.
down_payment_amount=(purchase_price*down_payment_percentage)/100
insurance_cost=((purchase_price-down_payment_amount)*insurance_rate)/100
principal_amount=purchase_price-down_payment_amount+insurance_cost
down_payment_amount_round=round(down_payment_amount)
insurance_cost_round=round(insurance_cost)
principal_amount_round=round(principal_amount)
print(f"Down payment is ${down_payment_amount_round}")
print(f"Mortgage insurance price is ${insurance_cost_round}")
print(f"Total mortgage amount is ${principal_amount_round}")

#Mortgage term
mortgage_term=int(input("Enter mortgage term (1, 2, 3, 5, 10):"))

while(mortgage_term!=1 and mortgage_term!=2 and mortgage_term!=3 and mortgage_term!=5 and mortgage_term!=10):
    print("Please enter a valid choice")
    mortgage_term=int(input("Enter mortgage term (1, 2, 3, 5, 10):"))

#Mortgage period
mortgage_amortization_period=int(input("Enter mortgage amortization period (5, 10, 15, 20, 25):"))
 
while(mortgage_amortization_period!=5 and mortgage_amortization_period!=10 and mortgage_amortization_period!=15 and mortgage_amortization_period!=20 and mortgage_amortization_period!=25):
    print("Please enter a valid choice")
    mortgage_amortization_period=int(input("Enter mortage amortization period (5, 10, 15, 20, 25):"))

#Annual mortgage interest rate
if(mortgage_term==1):
    annual_mortgage_interest_rate=5.95
    annual_mortgage_interest_rate=float(annual_mortgage_interest_rate)
    annual_mortgage_interest_rate_value=5.95/100
elif(mortgage_term==2):
    annual_mortgage_interest_rate=5.90
    annual_mortgage_interest_rate_value=5.9/100
elif(mortgage_term==3):
    annual_mortgage_interest_rate=5.60
    annual_mortgage_interest_rate_value=5.6/100
elif(mortgage_term==5):
    annual_mortgage_interest_rate=5.29
    annual_mortgage_interest_rate_value=5.29/100
elif(mortgage_term==10):
    annual_mortgage_interest_rate=6.00
    annual_mortgage_interest_rate_value=6/100

#Monthly payment 
effective_monthly_rate=(((1+annual_mortgage_interest_rate_value/2)**2)**(1/12)-1)
n=12*mortgage_amortization_period
monthly_payment=principal_amount*(effective_monthly_rate*(1+effective_monthly_rate)**n)/(((1+effective_monthly_rate)**n)-1)
print(f"Interest rate for the term will be {annual_mortgage_interest_rate}%")
monthly_payment_round=round(monthly_payment)
print(F"Monthly payment amount is: ${monthly_payment_round}")

#if user wants to see amortization shedule 
amortization_schedule=input("Would you like to see the amortization schedule? (Y/N):")
while amortization_schedule not in ['y','Y','N','n']:
    print("Invalid Input,Type Y or N")
    amortization_schedule=input("Would you like to see the amortization schedule? (Y/N):")
if(amortization_schedule.lower()=='y'):
    month=1
    print("\t""\t""\t""Monthly Amortization Schedule")
    print( "  ""Month""\t""\t""Opening Bal""\t"" ""Payment""\t""Principal""\t""Interest""\t""\t""Closing Bal "  )
    total_monthly_principal_amount_round=0
    total_interest_amount=0
   
    while(month<=(mortgage_term*12)):
        #Monthly interest amount, monthly principal amount, closing balance, total monthly principal amount and total interest amount  
        principal_amount_round=round(principal_amount,2)
        monthly_interest_amount=principal_amount_round*effective_monthly_rate
        monthly_interest_amount_round=round(monthly_interest_amount,2)

        monthly_payment_round_2=round(monthly_payment,2)
        monthly_principal_amount=monthly_payment_round_2-monthly_interest_amount_round
        monthly_principal_amount_round=round(monthly_principal_amount,2)

        closing_balance=principal_amount_round-monthly_principal_amount_round
        closing_balance_round=round(closing_balance,2)

        total_monthly_principal_amount_round=total_monthly_principal_amount_round+monthly_principal_amount_round
        total_monthly_principal_amount_round_2=round(total_monthly_principal_amount_round,2)

        total_interest_amount=total_interest_amount+monthly_interest_amount_round
        total_interest_amount_round=round(total_interest_amount,2)
       

        print( f"{month:5d}           {principal_amount_round:10.2f}  {monthly_payment_round_2:10.2f}    {monthly_principal_amount_round:10.2f} {monthly_interest_amount_round:10.2f} {closing_balance_round:10.2f}")
        principal_amount=closing_balance
        month=month+1
    print("-"*100)
    print("-"*100)
    print(f' Total {total_monthly_principal_amount_round_2:.2f}    {total_interest_amount_round:.2f}')  