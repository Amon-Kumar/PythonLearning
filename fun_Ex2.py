# Create a function take three inputs from the user and find out greates number of three.
def gretest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))
gretest_number= gretest(num1,num2,num3)
print(f"{gretest_number} is gretest Number!")