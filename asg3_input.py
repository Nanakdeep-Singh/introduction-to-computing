#Question 1
print("Question 1")
text_input=input("Enter text here\n")
if (" " not in text_input):
    #Checks if the input is a single word
    char_counter={}
   
    for i in text_input:
        char_counter[i]=text_input.count(i)
    print(char_counter)
    #Stores the char and their occurence
else:
    #case where more than one word is entered
    word_counter={}
    j="" 
    for i in text_input:
        if i!=" ":
           j=j+i
           #cancatenates the individual characters to form a word
        else:
           word_counter[j]=text_input.count(j)
           j=""
           #adds the word to the counter and resests j to store another word
#Stores the words and their occurence
    print(word_counter)
#Question 2
print("Question 2")
dt=int(input("Day-"))
mth=int(input("Month-"))
yr=int(input("Year-"))

if(yr%4==0):
  if(yr%400==0):
    leap=True
  elif(yr%100!=0):
    leap=True
  else:
    leap=True 
else:
  leap=False 
#Checks if the year is a leap year

  
def last_date(month):
 if(month%2==1): 
   if(month<=7):
    lst_dt=31
   if(month>7):
    lst_dt=30
 if(month%2==0 and month!=2):
   if(month<=7):
    lst_dt=30
   if(month>7):
    lst_dt=31
 if(month==2):
   if leap==True:
     lst_dt=29
   if leap==False:
     lst_dt=28
 return lst_dt
#This function gives the last date of the month taking the month as the input

if(1<=mth and mth<=12 and 1<=dt and dt<=31 and 1800<=yr and yr<=2025):#given constraints
 if(dt<=last_date(mth)):
  if (dt==last_date(mth) and mth!=12):
    dt=1
    mth=mth+1
  elif(dt==31 and mth==12):
    dt=1
    mth=1
    yr=yr+1
  else:
    dt=dt+1
#Gives the next date
  print(f"Next Date is: {dt}/{mth}/{yr}")
 else:
   print('error')
#Question 3
print("Question 3")
n=int(input("enter number of elements\n"))
my_list=[]
for i in range(n):
    list_elemnt=int(input("enter number\n"))
    my_list.append(list_elemnt)
sq_list=[]
for i in my_list:
    sq_tup=(i,i**2)
#creates a tuple with its 2nd element square of the first
    sq_list.append(sq_tup)
print(sq_list)

#Question 4
print("Question 4")
marks=int(input("Marks in range 4 to 10\n"))
#specifies respective criteriafor the grade entered
if(marks>=4 and marks<=10):
  if(marks==4):
      grade="D"
      perf="poor"
  elif(marks==5):
      grade="C"
      perf="below Average"
  elif(marks==6):
      grade="C+"
      perf="average"
  elif(marks==7):
      grade="B"
      perf="good"
  elif(marks==8):
      grade="B+"
      perf="very Good"
  elif(marks==9):
      grade="A"
      perf="excellent"
  elif(marks==10):
      grade="A+"
      perf="outstanding"
else:
    print("error")
print(f"Your Grade is {grade} and your performance is {perf}.")

#Question 5
print("Question 5")
n=int(input("number:"))

a2z="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
  if 2*i<n:  
   j=a2z[:n-2*i]#selects the string of alphabets from A to the selected number
   
   print(" "*i,j)#" "*i allows it to take the inverted pyramid shape

#Question 6
print("Question 6")
i=input("Add an entry?(Y/N)\n")
std_dict_sid={}
std_dict_name={}
while i=="Y":
    sid=input('Enter SID\n')
    name=input("Enter name\n")
    std_dict_sid[sid]=name
    std_dict_name[name]=sid
    i=input("Continue?(Y/N)\n")
    #Repeatedly asks the user if the want to add an entry until they say N and creates two
    #dictionaries with flipped key value pairs
print('part a')
print(std_dict_sid)

print("part b")

list_sid=[]
list_names=[]
for i in std_dict_sid:
    list_sid.append(i)
    list_names.append(std_dict_sid[i])
 
list_names.sort()
list_sid.sort()
#creates two lists one sorted according to sid and the other according to names

sort_names=[]
for i in list_names:
    sort_names.append({std_dict_name[i]:i})
print(sort_names)
    #prints the list of key value pairs sorted according to the names

print("part c")
sort_sid=[]
for i in list_sid:
    sort_sid.append({i:std_dict_sid[i]})
print(sort_sid)
    #prints the list of key value pairs sorted according to thesid

print("part d")
sid_search=input("Enter Sid to search:")
print(std_dict_sid[sid_search])
#searches and prints the name corresponding to the sid

#Question 7
print("Question 7")

def fibo(n):
    if n==1 or n==2:
        return 1

    return fibo(n-1)+fibo(n-2)
#selects two consecutive values before of the recursion and adds them to give the fibbonaci number

n=int(input("Enter n\n"))

j=0
fibo_seq=[]
for i in range(1,n+1):
    fibo_seq.append(fibo(i))
    #creates a list of fibonacci seq until the nth term
    j=j+fibo(i)

print(fibo_seq)
print(j/n)

#Question 8
print("Question 8")
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

set_a=(set1 |  set2) - (set1 & set2)
#set of all elements that are in Set1 and Set2 but not both.
print("part a:",set_a)

set_b=(set1|set2|set3)-(set1&set2)-(set2&set3) -(set3&set1)
#set of all elements that are in only one of the three sets Set1,Set2 and Set3.
print("part b:",set_b)

set_c=(set1&set2)|(set2&set3)|(set3&set1)-(set1&set2&set3)
print("part c:",set_c)

list_d=[]
for i in set1:
  if i>=1 and i<=10: 
   list_d.append(i)
set_d=set(list_d)
#set of all integers in the range 1 to 10 that are not in Set1.
print("part d:",set_d)


list_e=[]
for i in (set1 | set2 | set3):
  if i>=1 and i<=10: 
   list_e.append(i)
set_eout=set(list_e)
#set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3.
print("part e:",set_eout)
