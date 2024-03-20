import sys
from datetime import date

vehicle_plates = []
credit_card_numbers = []

SECRET_PASSWORD = "password"

#Function for registration of new vehicles
def new_vehicle_registration():
    if len(vehicle_plates) < 50:
        print('The Parking lot has spaces for your vehicle')
        plate_number = input('Enter your vehicle\'s plate number: ')

        if not vehicle_confirmation(plate_number):
            credit_card_number = input('Enter your Credit Card Number ($4.00 charge): ')

            vehicle_plates.append(plate_number)
            credit_card_numbers.append(credit_card_number)

            print(f'Thank you! Your plate {plate_number} has been added to the parking lot.')

        else:
            print(f'{plate_number} is already registered.')

    else:
        print('The parking lot is full.')

#Function for confirmation of vehicle availability
def vehicle_confirmation(plate_number):
    return plate_number in vehicle_plates

#function for the present date
def current_date():
    current_date = date.today()
    formatted_date = current_date.isoformat()
    return formatted_date

#Function for the already registered vehicles
def display_registered_vehicles():
    if len(vehicle_plates) != 0:
        print(f'Registered vehicles for {current_date()}')

        print(f'{"="*20}')
        print('\tPlate')
        print(f'{"="*20}')

        with open('registered_vehicles.txt', 'w') as f:
            for plate in vehicle_plates:
                f.write(f'{plate}\n')
                print(f'\t{plate}')

        print(f'{"="*20}')

    else:
        print('The parking lot is empty!')

#Function for charges of vehicles that are parked daily.
def daily_charges():
    print(f'Daily parking summary for {current_date()}')

    print(f'{"="*70}')
    print('\tPlate\t\tCredit Card\t\tCharge in $')
    print(f'{"="*70}')

    with open('daily_charges.txt', 'w') as f:
        for i in range(len(vehicle_plates)):
            f.write(f'{vehicle_plates[i]}\t{credit_card_numbers[i]}\t4\n')
            print(f'{vehicle_plates[i]}\t\t{credit_card_numbers[i]}\t\t4\n')

    print(f'{"="*70}')
    print(f'Total\t\t\t\t\t\t\t{len(credit_card_numbers)*4}')

#Function to remove the registered vehicles
def remove_registered_vehicle(plate_number):
    if not vehicle_confirmation(plate_number):
        print(f'The plate number {plate_number} is not registered.')
    else:
        index_to_remove = vehicle_plates.index(plate_number)
        vehicle_plates.pop(index_to_remove)
        credit_card_numbers.pop(index_to_remove)

        print(f'The vehicle with plate number {plate_number} is removed.')

#Function to remove all the vehicles
def eliminate_all_vehicles():
    vehicle_plates.clear()
    credit_card_numbers.clear()

    print('All vehicles were removed and the lot is empty.')

#Function to print the main user
def print_user_menu():
    print('*'*40)

    print('''* Welcome to Park and Go Parking Application! *
    Park from 6 PM - Midnight for a flat fee of $4.00''')

    print('*'*40)

    print('''Select from the following options:
1- Register a vehicle
2- Verify vehicle registration
3- Display registered vehicles and save them to file
4- Display daily charges and save them to file
5- Remove a vehicle
6- Clear vehicles
0- Exit''')

    return input('>>> ')


user_choice = print_user_menu()

while user_choice != '0':
    match(user_choice):
        case '1':
            new_vehicle_registration()
            input('Press enter button to continue....')
            user_choice = print_user_menu()

        case '2':
            password_attempt = input('Enter your password: ')

            if password_attempt == SECRET_PASSWORD:
                plate_input = input('Enter the plate number: ')

                if vehicle_confirmation(plate_input):
                    print(f'The vehicle with plate number {plate_input} is registered in the lot.')
                    input('Press enter button to continue....')
                    user_choice = print_user_menu()
                else:
                    print('The vehicle is NOT registered.')
                    input('Press enter button to continue....')
                    user_choice = print_user_menu()
            else:
                print('Password is incorrect!')
                input('Press enter button to continue....')
                user_choice = print_user_menu()

        case '3':
            password_attempt = input('Enter your password: ')
            if password_attempt == SECRET_PASSWORD:
                display_registered_vehicles()
                input('Press enter button to continue....')
                user_choice = print_user_menu()

            else:
                print('Password is incorrect!')
                input('Press enter button to continue....')
                user_choice = print_user_menu()

        case '4':
            password_attempt = input('Enter your password: ')

            if password_attempt == SECRET_PASSWORD:
                daily_charges()
                input('Press enter button to continue....')
                user_choice = print_user_menu()
            else:
                print('Password is incorrect!')
                input('Press enter button to continue....')
                user_choice = print_user_menu()

        case '5':
            password_attempt = input('Enter your password: ')
            if password_attempt == SECRET_PASSWORD:
                plate_to_remove = input('Enter the plate number: ')
                remove_registered_vehicle(plate_to_remove)
                input('Press enter button to continue....')
                user_choice = print_user_menu()
            else:
                print('Password is incorrect!')
                input('Press enter button to continue....')
                user_choice = print_user_menu()

        case '6':
            password_attempt = input('Enter your password: ')
            if password_attempt == SECRET_PASSWORD:
                eliminate_all_vehicles()
                input('Press enter button to continue....')
                user_choice = print_user_menu()
            else:
                print('Password is incorrect!')
                input('Press enter button to continue....')
                user_choice = print_user_menu()

        case _:
            print('Invalid input!!')
            input('Press enter button to continue....')
            user_choice = print_user_menu()