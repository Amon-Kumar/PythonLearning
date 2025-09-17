# Creat a function syntax:- 
''' 
    def function_name():
            # code block
            return result
'''
# Creat a function without parameter and without return value only use of print.
def my_function():
      print("Hello My Function")
my_function()

print("--------------------------------")
# Create a function with two parameters and use addition of return value.
def my_add(a,b):
    return a+b
add=my_add(5,4)
print("add: ",add)

print("--------------------------------")

# find the last character of the word with the help of function.
def last_char(name):
     return name[-1]
print("Last Char: ",last_char("Amon Kumar"))

print("--------------------------------")
# even odd
'''
def even_odd(num):
     if num%2==0:
          return "Even"
     else:
          return "Odd"
print("Even and odd value is : ",even_odd(112) )

2nd Method
'''
def even_odd(num):
    if num%2==0:
         return "Even"
    return "Odd"
print("Even and odd value is : ",even_odd(112) )

# 3rd Method
def is_even(num):
    if num%2==0:
        return True
    return False
print(is_even(10))

# 4rd Method
def odd_even(num):
     return num%2==0
print("Even or Odd value is: ", odd_even(12))