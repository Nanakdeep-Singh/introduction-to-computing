#Q1
print("Q1")
def twr_h(n , start,other,end):
    if n==1:
        print (f"Move disk 1 from {start} to {end}")
        return
    twr_h(n-1, start,end,other)
    print (f"Move disk {n} from {start} to {end}")
    twr_h(n-1,other,start,end)
#based on a pattern that emerges when looking at solution for the puzzle for different number of disks 
twr_h(3,'A','B','C')
#here A,B,C are the towers where the disksa are intially at a and finally at c

#Q2
print('Q2')
#Using iteration
print("Iteration")
n=7
lst=[] 
for i in range(1,n+2):
    if i==0:
       lst.append([1])
    elif i==1:
       lst.append([1,1])
    else:
      lst2=[]
      for j in range(i):
        if j==0 or j==(i-1):
          lst2.append(1)
        else:
          lst2.append(lst[i - 2][j - 1] + lst[i - 2][j])
          #selects 2 adjacent values from the level above and adds them
      lst.append(lst2)

for i in range(n+1):
  print(" "*(n-i),end="")
  for j in range(i+1):
    print(lst[i][j],end=" ")
  print("\n") 
#prints out the pascal triangle in form of a triangle


#Using Recursion
print("Recursion")
def pascal_triangle(t):
 def pascal(n):
    if n==0:
        return[1]
    if n==1:
      return [1,1]
    lst1=[]
    for i in range(n):
        if i==0 or i==(n-1):
          lst1.append(1)
        else:
          lst1.append(pascal(n-1)[i-1]+pascal(n-1)[i])
        #selects 2 adjacent values from the level above and adds them
    return lst1
 for i in range(t+2):
  print(" "*((t+1)-(i)),end="")
  for j in range(i):
   print(pascal(i)[j],end=" ")
  print("\n")  
pascal_triangle(4)

#Q3
print('Q3')
class Student:
   def __init__(self,name,roll_no):
       self.name=name
       self.roll_no=roll_no
       print('attributes for class were created')
   def __del__(self):
       self.name
       self.roll_no
       print("The attributes for class was deleted")
    
s1=Student("Akash",210)
print(f"The name of the student is{s1.name} and he/she has roll number{s1.roll_no}")
del s1
print("The object was deleted")

#Q4
print("Q4")
n1=int(input("Enter number 1 here:"))
n2=int(input("Enter number 2 here:"))
Quo=n1//n2
Rmdr=n1%n2
print(f"The quotient for the given inputs is{Quo}")
print(f"The remainder for the given inputs is{Rmdr}")
#part a
#to check wether a function is callable we use callable function
print(f"{callable(Quo)},Quotient is not callable")
print(f"{callable(Rmdr)},Remainder is not callable")

#part b
if n1==0 and n2==0 and Quo==0 and Rmdr==0:
    print("All values are zero")
else:
    print("Not all values are zero")

#part c
sum_list=[4,5,6,Quo,Rmdr]
out=[]
for i in sum_list:
   if i>4:
       out.append(i)
print(f"The values greater than 4 are {out}")
#filters out values greater than 4

#part d
out_set=set(out)
#creates the set of prev output
print(out_set)
#part e
out_imm=frozenset(out_set)
print(out_imm)
#part f
print(" Hash value of the max value is", hash(max(out_imm)))

#question 5
print("Q5")
class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
e1=Employee("Mehak",40000)
e2=Employee("Ashok",50000)
e3=Employee("Viren",60000)
#creates three objects employee 1, 2 and 3
e1.salary=70000
#updates the salary of employee1
print(f"The salary of {e1.name} is {e1.salary}")

del e3
print("Employee 3 Viren was deleted")

#Q6
print("Q6")
plyr1=input("Enter word here:")

def anagrams(s):
    if s == "":
        return set([s])
    else:
        ans =[]
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                    ans.append(w[:pos]+s[0]+w[pos:]) 
        return set(ans)
#returns the set of all the words possible from the word player1 gave 
plyr2=input("Enter word here Player 2:")

if plyr2 in anagrams(plyr1):
    print("YES!!your friendship is real:D")
else:
    print("Your friendship is fake :(")
