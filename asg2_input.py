#Question1
print("Question 1")
string_input="Python is a case sensitive language"

#part a
print("The length of the string is",len(string_input))
#Displays the length of the string

#part b
print(string_input[::-1])
#The third int in [::-1] reverses the order of the string

#part c
print(string_input[10:26])
#Selects the characters from the index 10 to the character at index 25

#part d
print(string_input.replace("a case sensitive","object oriented"))
#Replaces the selected text with the second argument

#part e
print(string_input.find("a"))
#Displays the index of "a"

#part f
print(string_input.replace(" ",""))
#Replaces all spaces with "".

#Question 2 
print("Question 2")
name=input('Enter your name here\n')
sid=input('Enter your sid here\n')
branch=input('Enter your department name here\n')
cgpa=input('Enter your cgpa here\n')

print('''Hey,%s Here!
My SID is %s
I am from %s department and my CGPA is %s'''%(name,sid,branch,cgpa))
#%s stands as a place holder for an input string

#Question 3
print("Question 3")
a=56
b=10

#part a
print("a&b=",a&b)
#Takes out the common values binary

#part b
print("a|b=",a|b) 

#part c
print("a^b=",a^b)
#Gives out the value that is either in a or in b

#part d
print("after left shift a=",a<<2,", after left shift b=",b<<2)

#part e
print("after right shift a=",a>>2,', after right shift b=',b>>4)

#Question 4
print("Question 4")
num1=int(input("Enter 1st number here\n"))
num2=int(input("Enter 2nd number here\n"))
num3=int(input("Enter 3rd number here\n"))

if(num1>num2):
   if(num1>num3):
 #If 1st number is larger than 2nd number and 3rd number then 1st number is largest
       print(num1,"is the greatest number") 
   else:
#but if the 2nd condition is false i.e. 3rd number is greater than 1st then 3rd lumber is the largest
       print(num3,"is the greatest number")
else:
#This else statement represts the case when 2nd number is greater than or equal to 1st number
    if(num2>num3):
# Now if num2 is greater than 3 then num 2 is the greatest   
        print(num2,"is the greatest number") 
    else:
#otherwise, num3 will be the greatest number
        print(num3,"is the greatest number")

#Question 5
print("Question 5")
text=input("enter text here\n")

if('name' in text):
#this statement checks whether the keyword is in the text
  print("Yes")
else:
    print("No")

#Question 6
print("Question 6")
side_a=int(input("Enter side length a\n"))
side_b=int(input("Enter side length b\n"))
side_c=int(input("Enter side length c\n"))

if(side_a>side_b+side_c or side_b>side_c+side_a or side_c>side_a+side_b):
#This statement checks for the condition whether the sum of two sides is greater than any one side
    print("No")
else:
    print("Yes")
#If the condition from if statement is false a triangle can be formed with the given sides
