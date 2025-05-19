# 01 find positive numbers

# number = [1,-2,3,-4,5,-6,7,-8,9,-10]

# positive_number = 0

# for num  in number:
#     if(num > 0):
#        positive_number += 1
# print(f'postive numbers are {positive_number}')

# 02 Sum of Even numbers

# userNumber = 10
# sum = 0

# for num in range(1 , userNumber+1):
#     if num % 2 == 0:
#         sum +=1

# print(f'Sum of even number is {sum}')

#03 print the multipication table of a given number up to 10,but skip number 5

# value = 3

# for num in range(1,11):
#    if num == 5:
#     continue
#    print(f'{value} X {num} = {value*num}') 

# 04 reverse a string

# userName = 'Sharjeel'
# reverse_userName = ''

# for letter in userName :
#     reverse_userName = letter + reverse_userName

# print(reverse_userName)

# 05 Find a first non-repeated character

# inp_str = 'teeteradsdfs'

# for char in inp_str:

#     if inp_str.count(char) == 1:
#         print(char)
#         break
    

# 06 Facrorial of a number

# num = 5
# factorial = 1

# while num > 0:
#     factorial *= num
#     num -= 1

# print(f'Factorial of 5 is {factorial}')

# 07 validate input


# while True:
#     userInput = int(input("Enter number please: "))
#     if 1<= userInput <=10:
#         print(f'Your entered value {userInput} and its correct')
#         break
#     else:
#         print(f'Your entered value {userInput} is wrong please retry')

# 08 prime number  checker

# userNumber = int(input('Enter number to check: '))

# is_Prime = True

# if userNumber > 1:
#     for num in range(2,userNumber):
#         if (userNumber % 2) == 0:
#             is_Prime = False
#             break

# if is_Prime == True:
#     print(f'Your entered number {userNumber} is prime')
# else:
#     print(f'Your entered number {userNumber} is not prime')

# 09 dublicate elemnent checker

# items = ['apple','bannana','orange','apple','mango','mango']
# uniqueItem = set()
# for i in items:
#     if i in uniqueItem:
#         print('dublicate', i)
#         break
#     uniqueItem.add(i)


# 10 wait time
import time

max_attempt = 5
wait_time = 1
atempts = 0

while atempts < max_attempt:
    print(f'Attempt is {atempts + 1 } and wait time',wait_time)
    time.sleep(wait_time)
    wait_time *=2
    atempts+=1
