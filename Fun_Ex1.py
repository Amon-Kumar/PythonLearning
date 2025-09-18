# Creat a function two inputs from the user than gretest num print that.
def great_num(a,b):
    if a>b:
        return "A is greater than B"
    # else:
    return "B is greater than A"
# greater = great_num(15,20)
# print(greater)
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
print(great_num(num1,num2))