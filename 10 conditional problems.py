#01 age calculator

# age = int(input('Enter your Age: '))

# if age>60 :
#     print(f'Your {age} and Senior ')
# elif 20 <=  age <=59:
#     print(f'Your {age} and Adult ')
# elif 13<=  age <=19:
#     print(f'Your {age} and Teenager ')
# else :
#     print(f'Your {age} and Child ')
    

#02 ticket price calculator

# age = int(input('Enter Your Age: '))
# day = 'wednesday'


# price = 12 if age>=18 else 8

# if day == 'wednesday':
#       print(f"Ticket price is ${price-2}")
# else:
#     print(f"Ticket price is ${price}")


# 03 Grade calculator

# scoure = int(input('Enter your Scoure: '))
# if scoure>100:
#     print("Please enter scoure btw 1-100")
#     # breakpoint
#     exit()
# elif  scoure >= 90:
#     print(f'Your scoure is {scoure} and Grade is A')
# elif  scoure  >= 80:
#     print(f'Your scoure is {scoure} and Grade is B')
# elif  scoure  >= 70:
#     print(f'Your scoure is {scoure} and Grade is C')
# elif  scoure  >= 60:
#     print(f'Your scoure is {scoure} and Grade is D')
# else:
#     print(f'Your scoure is {scoure} and Grade is F')


# 04 fruit condition checker
fruitColor = str(input("Enter fruitColor Name: "))

if fruitColor.upper() == 'Green'.upper():
    print('Banana is Unripe')
elif fruitColor.upper() == 'YEllow'.upper():
    print('Banana is ripe')
elif fruitColor.upper() == 'browN'.upper():
    print('Overripe')
else:
    print('property does not exists')
