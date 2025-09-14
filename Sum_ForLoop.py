# Sum of the 1 to 10 numbers
# total = 0
# for i in range(1,11):
#     total+=i
# print(total)

# ---------------------------------------------------------------------------------

total = 0
user_choice = input("Enter a Sum of the number  1 to 100:")
user_choice = int(user_choice)
for i in range(1,user_choice+1):
    total += i
print(total)

# ------------------------------------------------------------------------------------
# how to check user input one character count in a word or paragraph
name = input("Enter a Name: ")
temp = ""
for i in range(1,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp += name[i]

