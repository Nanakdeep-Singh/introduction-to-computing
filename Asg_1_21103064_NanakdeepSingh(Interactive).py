Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
number_1=int(input("Enter number 1:"))
Enter number 1:100
number_2=int(input("Enter number 2:"))

Enter number 2:73
number_3=int(input("Enter number 3:"))
Enter number 3:66
average=(number_1+number_2+number_3)/3

print(average)
79.66666666666667

==================================== RESTART: Shell ====================================
gross_income=float(input("Enter Gross income to the nearest penny :$"))
Enter Gross income to the nearest penny :$1537329.05
dependents=int(input('Enter the number of dependents:'))
Enter the number of dependents:3
taxable_income=gross_income-10000-dependents*3000
income_tax=taxable_income*20/100
print('Your income tax is',income_tax)
Your income tax is 303665.81

==================================== RESTART: Shell ====================================
credentials=[21103064,"Nanakdeep",'M',"Intro the computing",8.7]
print(credentials)
[21103064, 'Nanakdeep', 'M', 'Intro the computing', 8.7]

==================================== RESTART: Shell ====================================
student_1=float(input("Enter marks student 1:"))
Enter marks student 1:100.00
student_2=float(input("Enter marks student 2:"))
Enter marks student 2:72.98
student_3=float(input("Enter marks student 3:"))
Enter marks student 3:12
student_4=float(input("Enter marks student 4:"))
Enter marks student 4:47.80
student_5=float(input("Enter marks student 5:"))
Enter marks student 5:77
marks_list=[student_1,student_2,student_3,student_4,student_5]
marks_list.sort()
print(marks_list)
[12.0, 47.8, 72.98, 77.0, 100.0]

==================================== RESTART: Shell ====================================
color_list=["Red","Green",'White','Black','Pink','Yellow']
color_list.pop(3)
'Black'
print(color_list)

['Red', 'Green', 'White', 'Pink', 'Yellow']

==================================== RESTART: Shell ====================================
color_list=["Red","Green",'White','Black','Pink','Yellow']
color_list[3:5]=['Purple']
print(color_list)
['Red', 'Green', 'White', 'Purple', 'Yellow']

==================================== RESTART: Shell ====================================
