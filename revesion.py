# postive nums
# nums = [1,2,3,4,-3,-2,-6,8,-3]

# postivieNums = 0

# for i in nums:
#     if i > 0:
#         postivieNums+=1

# print(postivieNums)

# sum of even nums

# nums = 10
# sum = 0

# for i in range(1,11):
#     if i % 2 == 0:
#         sum+=i
# print(sum) 


# Table

# table = 5

# for i in range (1,11):
#     print(f'{table} x {i} = {table*i}')


# reverse a string

# name= 'sharjeel'
# reverseStr = ''

# for i in name:
#     reverseStr =  i + reverseStr 

# print(reverseStr)

# non repeated character

# str = 'turttlees'

# for i in str:
#     if str.count(i) == 1:
#         print(i)
#         break


# factorial calculator

# num = 5
# factorial = 1

# while num > 0:
#     factorial *= num
#     num -= 1

# print(f'Factorial of 5 is {factorial}')

# input validation

# value = True

# while value:
#     user = int(input('Please guess number: '))
#     if 1 <= user <= 10:
#         print('You Guess a coreect number btw 1-10')
#         value= False
#     else:
#         print('Guess Again')


#  prime number checker

user = int(input('Enter Number:'))
isPrime = False

if user > 1:
    for i in range(1,user):
        if (i % 2) == 0:
            isPrime = True 
            break
        
if isPrime == True:
    print('Your number is prime')
else:
    print('your number is not prime')