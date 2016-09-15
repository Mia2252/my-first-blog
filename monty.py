import random

correct = 0

for i in range(10000):
    correct_door = random.randint(1,3)
    choice = random.randint(1,3)

    if correct_door == choice:
      correct=correct+1

    opendoor = random.randint(1,3)
    while opendoor == correct_door or opendoor == choice:
        opendoor = random.randint(1,3)



print(correct)
