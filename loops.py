
course = 'python for beginners'

print(course.upper())
print(course.lower())
print(course)

print('---------------------------------------------')

course = 'python for beginners'
print(course.replace('beginners', 'Absolute Beginners'))
print(course.replace('p', 'T'))
print('python' in course)

print('-----------------------------------------------')

print('Arithmetic operations')
print(10 % 3)
print(10 // 3)
print(10 ** 3)
x = 10
x = x + 3
print(x)
x -= 3
print(x)

print('-----------------------------------------------')

x = (10 + 3) * 2 ** 2
print(x)

print('-----------------------------------------------')
print('maths functions')
x = 2.9
print(round(x))
print(abs(-2.9))

import math

print(math.ceil(2.9))
print(math.floor(2.9))

print('-----------------------------------------------')

print('if statement')
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
    print("Enjoy your day")

print('-----------------------------------------------')

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")

print('-----------------------------------------------')

print('logical Operators')
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print('Eligible for loan')

print('----------------------------------------------')

print('Comparison Operators')
temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

print('----------------------------------------------')

name_character = 50

if name_character < 3:
    print("Name must be at least 3 characters")
elif name_character > 50:
    print("Maximum character exceeded")
else:
    print("Name looks good")

print('----------------------------------------------')

name = "Ayoyiwaka Awodele"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must not exceed 50 characters")
else:
    print("Name looks good")

print('----------------------------------------------')

print('For Loop')
for item in ['mosh', 'John', 'Sarah']:
    print(item)
for item in range(2, 10, 2):
    print(item)

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")
print('----------------------------------------------')

print('nested loops')

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

print('----------------------------------------------')

numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

print('----------------------------------------------')

print('List')

names = ['Bisi', 'Dayo', 'Yetunde', 'Bola', 'Tope', 'Bimbo', 'Tayo']
names[0] = 'Big Mummy'
print(names[3:6])
print(names)

print('while loops')


print('----------------------------------------------')
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


print('----------------------------------------------')

print('2-dimensional List')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:

    for item in row:
        print(item)
print('----------------------------------------------')

print('List Methods/Functions')

numbers = [5, 2, 1, 5, 7, 4]
numbers.insert(0, 10)
numbers.remove(1)
numbers.pop()
numbers.sort()
numbers.reverse()
print(numbers)
print('----------------------------------------------')
print('Remove Duplicates')

print("-----------------------------------------------")
print('Turples')
print("Like list but can't be modified")
print("We can only get info about a turples, it can't be changed")
numbers = (1, 2, 3)

print(numbers)
print('------------------------------------------')
print('Unpacking')

coordinates = (1, 2, 3)

x, y, z = coordinates
print(y)
print("------------------------------------")
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "'_'",
    ":(": "'/'"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)