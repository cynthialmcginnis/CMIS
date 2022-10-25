

# Introduction to Python

# In[ ]:


print("What is a variable?\n")


# When we run the code above, Python will output “What is a variable?” and then forget it. However, we often need Python to remember what we tell it. Variables tell Python to remember something so we can use it later.
# 

# In[ ]:


question = "What is a variable?"


# In[ ]:


question


# In[ ]:


print(question)


# In[ ]:


answer = "  A variable is a value that can change."


# In[ ]:


print(question+answer)


# In[ ]:


print(my_name)
my_name = "Joe"


# Why is there an Error?

# In[ ]:


my_name = "Joe"
print(my_name)


# In[ ]:


print("My name is",my_name,".")


# Variable Names:  
# 
# Variable names should start with a letter. 
# Use Camel Case.
# Some words in Python are reserved.

# In[ ]:


my_name = "Luke"
myName = "Luke too"


# In[ ]:


my_name
myName


# In[ ]:


#Notice in the above code my_name didn't print.  Only the last line will print.


# In[ ]:


''' Making comments 
    so that your code
    is easy to understand '''


# In[ ]:


"""Make comments so
that your code is easy to understand."""


# In[ ]:


##Make comments
so your code is easy to understand


# Why is there an error?

# In[ ]:


#Make comments
#so your code is easy to understand


# In[ ]:


color = 'blue'  # assign a value to color
eyeColor = color # assign color to eyeColor
print(eyeColor)


# In[ ]:


type(color)  # What is the variable type?


# #String str
# #Int integer
# #float floating point

# In[ ]:


hugeNumber = "900000"
my_number = 900000
myOtherNumber = 900000.00


# In[ ]:


print(type(hugeNumber))
print(type(my_number))
print(type(myOtherNumber))
      


# In[ ]:


76trombones = "76"  #What happens?  Why?


# In[ ]:


trombones@76 = 76 #What happens?  Why?


# In[ ]:


class = "Python"  ##What happens?  Why?


# In[ ]:


trombone76 = 76


# In[ ]:


MyClass = "Python"


# In[ ]:


print(trombone76, MyClass+"s")


# Reserved words:
# and del from not while as elif global or with assert else if pass yield break except import print class exec in raise
# continue finally is return def for lambda try

# A statement is a unit of code that the Python interpreter can execute. 
# We haveseen two kinds of statements: print and = .  The = sign does not mean the same when writing code as it does in arithmetic.  = is an assignment.
# If I write x = 2, this means that 2 is stored in memory in the variable x.
# 
# A script usually contains a sequence of statements.

# In[ ]:


x = 2
y = 3
x + y


# In[ ]:


x - y


# In[ ]:


print("xy=", x*y)


# In[ ]:


type(x*y)


# In[ ]:


y/x


# In[ ]:


type(y/x)


# In[ ]:


x = 10
x%y # Modular Arithmetic 10/3 has a remainder of 1:  3*3 + 1 = 10 


# In[ ]:


y%x  # 3/10 has a remainder of 3:  0*3 + 3 = 3


# In[ ]:


3**2 # 3 to the exponent of 2


# In[ ]:


x//y #Truncated Division 10/3 = 3 + 1/3 Returns the whole part


# In[ ]:


num1="10"
num2="20"
print(num1+num2)


# In[ ]:


type(num1+num2)


# In[ ]:


type(int(num1+num2)) #change a string to an integer


# In[ ]:


my_str = num1+num2
my_number = int(num1)+int(num2)


# In[ ]:


print("My string is ",my_str,'\n', "My_number \t", my_number)


# In[ ]:


my_str+my_number  #What happens?  Why?


# In[ ]:


my_str+str(my_number)


# In[ ]:


int(my_str) + my_number


# Input data

# In[ ]:


input("How is your day going?\n")


# In[ ]:


my_day = input("How is your day going?\n")


# In[ ]:


print("My day is "+my_day)


# In[ ]:


for letter in my_day: # note the semicolon 
    print(letter)


# In[ ]:


i = 0  #declare the counter
for letter in my_day:
    i= i+1
    print(i)


# In[ ]:


print(i)


# In[ ]:


def my_day():
    myDay = input("How is your day going?")
    return myDay
    


# In[ ]:


myDay = my_day()


# In[ ]:


print(myDay)


# In[ ]:


def num_letters(x):      # define a function that counts the letters in a sentence
     i = 0
     for letters in x:
        i = i + 1
     return i
    


# In[ ]:


num_letters(myDay)


# In[ ]:


myDay = my_day()


# In[ ]:


num_letters(myDay)


# Boolean Expressions
# 
# x != y # x is not equal to y
# x > y # x is greater than y
# x < y # x is less than y
# x >= y # x is greater than or equal to y
# x <= y # x is less than or equal to y
# x is y # x is the same as y
# x is not y # x is not the same as y

# In[ ]:


print("x = ",x, "y = ", y)
x != y


# In[ ]:


x > y


# In[ ]:


x < y


# In[ ]:


x is y


# In[ ]:


x is not y


# In[ ]:


x == x


# In[ ]:


'blue' == 'blue'


# In[ ]:


'Blue' == 'blue'


# In[ ]:


if x > y:
    print("x is greater than y by", x-y, "units.")  #Conditional statement


# In[ ]:


if x == y:
    print("x and y are equal")
else:
    print("The difference between x and y is", x -y)


# In[ ]:


if x == y:
    print("x and y are equal")
elif x > y:
    print("x is larger than y")
else: 
    print("x is smaller than y")
    


# In[ ]:


def compNum(x,y):
    if x == y:
        print("x and y are equal")
    elif x > y:
        print("x is larger than y")
    else: 
        print("x is smaller than y")
    return
    


# In[ ]:


compNum(2,5)


# In[ ]:


compNum(5,5)


# In[ ]:


compNum(8,4)


# Discussion
# Create a Python program that accepts at least three values as input.  The program must include an if statement that performs two different computations based on the value of the first input. The computations should involve the values of the second and third values input. It should then display the result of the computation.

# In[ ]:


myFoodChoice = input("What do you want to eat for lunch?, type I for Italian, B for Burgers or C for Chinese")


# In[ ]:


if myFoodChoice == "I":
    print("Great!  I know of an Italian place you'll love!")
elif myFoodChoice == "B":
    print("Good Choice!")
elif myFoodChoice == "C":
    print("I love Chineese food!")
else:
    print("You didn't follow diretions!")
    


# In[ ]:


x = int(input("Enter a number between 0 and 9"))
y = int(input("Enter a number between 0 and 9"))
z = int(input("Enter a number between 0 and 9"))


# In[ ]:


if x <= y and x != 0:
    sumNums = x + y + z
    print("The sum of the numbers is",sumNums)
elif x > y or x > z:
    subtractNums = x - y - z
    print("x - y - z =",subtractNums)
else:
    multNums = x*y*z
    print("The product of the numbers is",multNums)


# In[ ]:


myTemp = input("What is the temperature out today in degrees farenheight?")


# In[ ]:


if int(myTemp) >= 78 and int(myTemp) <=88:
    print("Just Right!")
elif int(myTemp)< 78:
    print("Too Cold")
else:
    print("Too hot!")
    




