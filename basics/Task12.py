import random
def game(a, b):
    first_random = random.randint(a, b)
    second_random = random.randint(a, b)

    index = [first_random,  second_random]
    print(r)
    while True:

        user_answer = input()
        if(r != ord(user_answer) -ord("0")):
            print("Try again!")
        else:
            print("congratulate !")
            break



game(1, 5)
