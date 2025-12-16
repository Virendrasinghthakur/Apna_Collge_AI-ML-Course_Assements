# Q1 write a program that ask the user for their name and agr ,then print a sentecnde

# name=input('enter your name :')
# age=int(input('enter your age :'))
# print('Hello {}, you are {} years old'.format(name,age))


# Q2 take two numbers as input from the user and print their sum ,diffrence ,product,and quotent

# num1=int(input('enter the first number :'))
# num2=int(input('enter the second number :'))
# sum=num1+num2
# diffrence=num1-num2
# product=num1*num2
# quotent=num1/num2
# print(f'the numbers are {num1} and {num2} \n their sum is {sum} \n diffrence is {diffrence} \n product is {product} \n quotent is {quotent}')


# Q3 ask the user to enter two integers and one float. Convert them all to floats and print their average.

# num1=int(input('enter num1 :'))
# num2=int(input('enter the second number :'))
# num3=float(input('enter the third number in float :'))
# num1=float(num1)
# num2=float(num2)
# print(f'the average of the numebers { num1},{num2} and {num3} by converting them all to float is {(num1+num2+num3)/3}')



#  Q4 the user enter a string containing a number  convert it into an int, float, string again  print all three values with their types

# a=input('enter the numberd string')
# b=int(a)
# c=float(a)
# d=str(a)
# print(type(a),type(b),type(c),type(d))

# Q4 evaluate and print the result of the following expressions 
# x=10+3*2**2

# print(10+3*2**2)


# Q6 write a program to swap values of two numbers entered by numbers

# a=int(input('enter the values of a:'))
# b=int(input('enter the values of b :'))
# print(f"before swapping a ={a} and b={b}")
# temp=a
# a=b
# b=temp
# print(f"After swapping a ={a} and b={b}")


# Q7 convert the tempearatur from celcius to fahrenhiet

# temperature=input('enter the tempearute in Celsius :')
# temperature=float(temperature)
# fahrenheit=(temperature*(9/5))+32
# print(f'The temperature is {fahrenheit} fahrenhiet')


# Q8 take the radius from user and print the area of the circle

# r=int(input('enter the radius of the circle:'))
# area=3.14*r**2
# print(f'the area of the circle with radius ={r} is {area}')

# Q9 ask the user for principal,rate and time.convert all to float and compute simple intreset:

# p=float(input('enter the principal values :'))
# r=float(input('enter the rate of interest :'))
# t=float(input('enter the period of time :'))
# si=(p*r*t)/100
# print(f'the simple intrest is {si}')

# Q10 take a decimal number as input and output it in int and fractionsl part

num=float(input('enter the decimal value :'))
print(f'the intger part is {int(num)} and the fractional part is {num%1}')