# Question 1: Cube Number Test... Print out all cubed numbers up to the total value 1000.
# Meaning that if the cubed number is over 1000 break the loop.
list_num = []

# 0
# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
# 1000

list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cube_list = []
for i in list_num:
    cube = i**3
    cube_list.append(cube)

print(cube_list)
if list_num == 10:
    print('too much')

# Question 2: Get first prime numbers up to 100
# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

for i in range(3-101):
    if i % 1 == 25:
        print('hi im prime')
        i += 1


# if 10 > 10000:
#     print('hello')
else:
    print('Goodbye')

# Question 3: Take in a users input for their age, if they are younger than 18
# print kids, if they're 18 to 65 print adults, else print seniors

age = input('what is your age? ')

print(age, type(age))

if int(age) <= 17:
    print('kids')
elif int(age) >= 18 <= 65:
    print('adults')
else:
    print('Seniors')


# An elif only runs when the if (or elif) directly above it evaluates to False
