#Question_1
number_1=int(input("Enter number 1:"))
number_2=int(input("Enter number 2:"))
number_3=int(input("Enter number 3:"))

average=(number_1+number_2+number_3)/3
#finds the average of the numbers

print(average)


#Question_2
gross_income=float(input("Enter Gross income to the nearest penny :$"))
dependents=int(input('Enter the number of dependents:'))

taxable_income=gross_income-10000-dependents*3000
income_tax=taxable_income*20/100
#Formula for calculating tax

print('Your income tax is',income_tax)


#Question_3
credentials=[21103064,"Nanakdeep",'M',"Intro the computing",8.7]
#creates a list of student credentials 

print(credentials)


#Question_4
student_1=float(input("Enter marks student 1:"))
student_2=float(input("Enter marks student 2:"))
student_3=float(input("Enter marks student 3:"))
student_4=float(input("Enter marks student 4:"))
student_5=float(input("Enter marks student 5:"))

marks_list=[student_1,student_2,student_3,student_4,student_5]


marks_list.sort()
#sorts students according to the marks they entered
 
print(marks_list)


#Question_5a
color_list=["Red","Green",'White','Black','Pink','Yellow']
color_list.pop(3)
#removes the item at index(3) from the list

print(color_list)


#Question_5b
color_list=["Red","Green",'White','Black','Pink','Yellow']
color_list[3:5]=['Purple']
#replaces black and pink with purple

print(color_list)


