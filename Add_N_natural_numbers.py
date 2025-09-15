# Write a program user input n number and print the add n natural numbers.
num = int(input("Enter a Natural Number: "))
i = 1
total = 0
while i <= num:
    total = total +i
    i = i+1
print(f"Total Natural Number: {total}")