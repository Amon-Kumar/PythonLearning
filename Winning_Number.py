winning_number = 25
user_input = int(input("Gass a Number Game 1 to 100: "))
if user_input == winning_number:
    print("!..You Win..!")
else:
    if user_input > winning_number:
        print("To High Number")
    else:
        print("To Low Number")