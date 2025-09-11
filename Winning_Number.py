# Guess a Number
# Make a variable, like winning_number and assign any to it.
# Ask user to guess a number:
#if user guessed correctly then print "! You Win !"
# if user didn't guessed correctly then:
    # if user guessed Higher than actual number then print "Too High"
    # if user guessed lower than actual number then print "Too Low"
winning_number = 25
user_input = int(input("Gass a Number Game 1 to 100: "))
if user_input == winning_number:
    print("!..You Win..!")
else:
    if user_input > winning_number:
        print("To High Number")
    else:
        print("To Low Number")