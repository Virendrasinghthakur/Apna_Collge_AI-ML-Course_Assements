# Q1. write a program that takes salary as input. using conditional statemnets, calculate the final tax reate on these rules;

# def salary(salary):
#     if salary<30000:
#         return salary*5/100
#     elif salary>30000 and 70000>salary:
#         return salary*15/100
#     else:
#         return 70000*25/100 
# print(salary(50000))

# Q2. write a function that takes two intger a and b and prints all even numbers betweeen them.

# def even_num(a,b):
#     for i in range(a,b):
#         if i%2==0:
#             print(i)
# print(even_num(1,10))


# Q3. write a function that print the digits of number,n.
# def print_digit(num):
#     while(num):
#         print(num%10)
#         num=num//10

# print(print_digit(312))


# Q4. write a function to return the count the number of digit in a number n.
# def count_dig(num):
#     count=0
#     while(num):
#         count+=1
#         num=num//10
#     return count
# print(count_dig(122))

# Q5. write a function to return the sum of digit of a number ,n.
# def sum_dig(num):
#     sum=0
#     while(num):
#         sum+=num%10
#         num=num//10
#     return sum
# print(sum_dig(222))

# Q6. write a progem to print all number from 1 to 100 that are divisible by both 3 and 5.
# def num():
#     for i in range(1,100):
#         if i%3==0 and i%5==0:
#             print(i)
# num()

# Q7. design a program to continuosly input a number n from user & print if it is positive or negative until the user enters 'quite'

# while True:
#     inp=input('enter a number or enter quite ')
#     if inp=='quite':
#         break
#     print(inp)

# Q8. let's create a simple calci that perform arithmetic operations . create a function calculator(a,b,operation) that performs additon,subtraction, multiplication,or division based on the operation para,eter

# def calci(a,b,operation):
#     if operation=='+':
#         return a+b
#     elif operation=='-':
#         return a-b
#     elif operation=='*':
#         return a*b
#     elif operation=='/':
#         return a/b
#     else :
#         return 'operationis not valid'

# print(calci(2,5,'+'))

# Q9. write a function is_prime that reutrns true if n is prime number and false otherwise,using a loop

# def is_prime(num)->bool:
#     if num<2:
#         return False
#     for i in range(2,num-1):
#         if num%i==0:
#             return False
#     return True

# print(is_prime(21))

# Q10. let's create a 'number gussing game'. given a secret number write a program that asks the users to gues it and prints

def guess_num(num):
    while True:
        g=input('enter quite to exit OR enter your guessed number :')
        if g=='quite':
            break
        if num<g:
            print( 'too high')
        elif num>g:
            print('too low')
        else:
            print('correct')
guess_num(15)

    