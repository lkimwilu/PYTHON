# number = 1
# name = "lyric"
 
#  print("name")

#  a, b, c = "self", 23, True
#  print(a, b, c)

# python is case sensitive


# site1 = site2 = "Shield.intl"

# print(site2)
# site 3 = "yooh"
# site 4 = site 3

# print(site4)


# languages = ["HTML", "JS", "PYTHON",3, True, None, 23, "Fel"]

    #  print(languages)

#  print(languages[-3]) 

# print(languages[1:6])  

# playstation = ("xBox", "controller", 400, True)

# print(playstation[2])

# def sum():
#  print(2 + 3)
# sum()

# def add_numbers():
#     print(2 + 3)

#     return answer

# add_numbers()


#  indentation is very important in python
    # return key word terminates any piece of code

# def add_sum(a, b):
#     c= a+b
#     return c
#     print(add_sum(1,2))

# FUNCTIONS
# def sum_args(*numbers):
#     sum = 0
#     for number in numbers:
#          sum += number
#     return sum
# print (sum_args(8, 8, 9, 5, 6))



# FUNCTIONS AND VARIABLE SCOOPS
# 1.Local scope

# Local scope refers to a variable declared inside a function.

# Example,
# def add_sum(a, b):
# answer = a + b
# return answer
# print(add_sum(12, 5))


# 2. Global scope
# 3. Global scope
# Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere.

# Example
# global_var = 13

# def add_nums(a, b):
#    total = a + b
#    print("Global Variable ", global_var)
#    def double_it():
#      #local var
#       double = total * 2
#       print("Global var in inner function: ", global_var)
#       print("Double: ", double)
#   double_it()
#   return total
# add_nums(13, 5)

myNumbers = (1, 3, 5)

def printGlobalScope():
  print("This is a list:", myNumbers)
printGlobalScope()





# 3.Enclosing scope
# Enclosing scope refers to a function inside another function or what is commonly called a nested function.

# Example
# def add_nums(a, b):
#   answer = a + b
#   def double_it():
#      double = answer * 2
#     print(double)
#  double_it()
#   return answer
# print(add_nums(12, 53))
# def enclosedScope(a, b):
#      answer = a + b 

#      def double_sum():
#           double_sum = answer * 2
#           print(double_sum)
#      double_sum()  
#      return answer
# print(enclosedScope(3, 5))


# 4.Built-in scope


