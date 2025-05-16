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
# fruitColor = str(input("Enter fruitColor Name: "))

# if fruitColor.upper() == 'Green'.upper():
#     print('Banana is Unripe')
# elif fruitColor.upper() == 'YEllow'.upper():
#     print('Banana is ripe')
# elif fruitColor.upper() == 'browN'.upper():
#     print('Overripe')
# else:
#     print('property does not exists')

# 05 Weather sugestion

# weather = str(input('Enter Weather: '))

# if weather.upper() == 'Sunny'.upper():
#     print('Go for a walk')
# elif weather.upper() == 'Rainy'.upper():
#     print('Read a book')
# elif weather.upper() == 'Snowy'.upper():
#     print('Build a snow man')    

# 06 distance calculator

# distance  = int(input('Enter Distance: '))

# if distance <= 3:
#     print('walking')
# elif distance <=15:
#     print('Bike')
# else:
#     print('Car')





# 07 coffe custmization

# coffe_size = str(input('Enter Coffe Size: '))
# extra_shots = True

# if extra_shots:
#     print(f"Here's your {coffe_size} with Extra Short")
# else:
#     print(f"Here's your {coffe_size} ")



# 08 password strenght checker

# password = str(input("Enter strong pass with minimum Length of 8 Chararcters:"))

# if(len(password) <6 ):
#     print('Weak Password')
# elif(len(password)  <= 10 ):
#     print('Medium password')
# elif(len(password)>10):
#     print('strong password')


# 09 leap yeaer checking

year = int(input('Enter Year: '))

if (year % 400 == 0 ) | (year % 4 == 0 and year % 100 != 0):
    print(f'{year} is Leap year')
else:
    print(f'{year} is not leap year')


# 10 animal food selection

# animnal = str(input('Enter Animal Name: ')).lower()
# animal_Age = int(input('Enter Animal Age: '))

# if animnal == 'cat' and animal_Age <= 2 :
#     print('Baby Cat food')
# elif animnal == 'cat' and animal_Age <= 5 : 
#     print('Senior cat food')
# elif animnal == 'dog' and animal_Age <= 2 : 
#     print('Puppy food')
# elif animnal == 'dog' and animal_Age <= 5 : 
#     print('Senior dog food')
# else:
#     print('Please enter name eg.dog and cat')
