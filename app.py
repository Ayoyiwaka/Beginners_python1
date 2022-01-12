
print("----------------------------------------")

print("Functions")

def greet_user():
    print('Hi There')
    print('Welcome aboard')


print ("Start")
greet_user()
print("Finish")
print('------------------------------------------')

print("Parameters")
def greet_isee(name):
    print(f'Hi {name}!')
    print('Welcome aboard')


print("start")
greet_isee("Yiwaka")
print("Finish")

print("--------------------------------------------")
print('Keyboard Arguement')
def greet_user(first_name, last_name):
    print(f'Hi{first_name} {last_name}!')
    print('welcome aboard')

print("Start")
greet_user(last_name="Awodele", first_name="Ayoyiwaka")
print("finish")

print("--------------------------------------------")
print('Use position arguements')
print('Return Statement')

def square(number):
    return number * number

print(square(3))

print("--------------------------------------------")
print('Creating reusable Functions')
print('Exceptions')

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid Value')