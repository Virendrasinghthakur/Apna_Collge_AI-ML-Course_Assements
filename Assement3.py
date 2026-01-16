#  Q1-ask a user for a string and check whearther it is a plindrome or not a 

# s=input("enter your string ")

# left=0
# right=len(s)-1
# while(left<right):
#     if s[left]!=s[right]:
#         print("not palindrome")
#         break
#     else:
#         left+=1
#         right-=1
# print("valid palindrome")

# Q2. given a list of two integers compute the average of all numbers in a list

# l=[12,13,25,18]
# print(sum(l))

# Q3. input two list of integers from the user.Merge them into one list and sort the result

# list1=[1,2,7]
# list2=[2,4,5]
# list3=list1+list2
# list3.sort()
# print(list3)


#Q4. given a tuple of integers, create a tuple of all even numbers,and odd numners

# tup=(1,5,6,8,3,9,7)
# odd=()
# even=()
# for t in tup:
#     if t%2==0:
#         odd+=(t,)
#     else:
#         even+=(t,)
# print(odd)
# print(even)

# Q5. create adictionary where keys=student names,values=marks write a menu based program where user presses a depending on the operation they want to perform on the dictionary

# def menu(self,dict):
#     inp=input("""
#         A.add a student
#         B.update marks
#         C.search student
#         D.Display all students and marks
# """).upper()
#     if inp=='A':
#         name=input("enter name of the student:")
#         marks=int(input("enter the marks of the students:"))
#         dict[name]=marks
#     elif inp=='B':
#         name=input("enter name of the student:")
#         marks=int(input("enter the marks of the students:"))
#         for s,m in dict.items:
#             if s==name:
#                 m=marks
#                 print("marks updated")
#             else:
#                 print("student not found")
#     elif inp=='C':
#         name=input("enter name of the student:")
#         print(dict[name],dict[marks])

#     elif inp=='D':
#         for s,m in dict.items:   
#             print(s,m)
#     else:
#         print("select a valid options")

#     self.menu(dict)

# dict={"abhay":20}
# menu(dict)


# Q6.
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# dict={}

# for word in words:
#     dict[word]=len(word)
# print(dict)