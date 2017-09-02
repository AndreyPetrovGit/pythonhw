import random
def game(a, b):
    r = random.randint(a, b)
    print(r)
    while True:

        user_answer = input()
        if(r != ord(user_answer) -ord("0")):
            print("Try again!")
        else:
            print("congratulate !")
            break



game(1, 5)
