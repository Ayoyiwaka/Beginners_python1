print('while loops')

guess_count = 1
while guess_count <= 5:
    print('*' * guess_count)
    guess_count = guess_count + 1
print("Done")

print('----------------------------------------------')
print("Guessing Game")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!!!")
        break
else:
    print('Sorry, you failed')


print('----------------------------------------------')

print('Car Games')
started = True
command = ""
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car already started!!!")
        else:
            started = True
        print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!!")
        else:
            started = False
        print("Car Stopped...")
    elif command == "help":
        print("""
 Start - To start the car
 Stop - To stop the car
 Quit - To quit
""")
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that!!!")

print("----------------------------------------")

print('For Loop')
