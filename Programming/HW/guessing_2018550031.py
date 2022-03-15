# 1에서 100 사이에 숫자를 guess 하는 게임
# n번의 기회를 이용, 처음 입력으로 받음
# 맞추면 "You won"
# 틀리면 "___is too high" 또는 "___is too low"를 출력
# n번의 기회를 다 사용하면 "You Lose"
# guessing_학번.py

"""Before you try this game, it would be better to know following notice
Notice
0. It is very desirable to run it with google colab because some results can show up after a current loop.
1. Do not ask me the answer. It is totally random so I don't even know it.
2. input the number of chanses do you wanna get.
3. input your guess.
4. if you are wrong, then input y or n. if it is y, you can see the average of your guess and answer.
5. Becareful!! if you get a hint at the last chance you should try again.
6. If you type wrong class or give up, you can get a sarcastic sentense. Sorry in advance."""
import numpy as np

def try_again(answer):
    import numpy as np
    """This is try_again module that asks whether you wanna try agaign or not when you lose your all chances"""
    if answer == 'y':
        try:
            answer = np.random.randint(0,100)
            n_trial = int(input("How many times do you want to try: "))
            for i in range(n_trial):
                guess = int(input("Please type from 0 to 100: "))
                avg = int((guess + answer)/2)
                if guess == answer:
                    print("You won")
                    again = input("Congrats!!, Do you wanna try again? y/n ")
                    try_again(again)
                    break
                elif guess > answer:
                    if guess > 2*answer:
                        print("Your guess:" + str(guess) + " is too high")
                        ask = input("You are wrong, do you want a hint?? y/n ")
                        if ask.lower() == 'y':
                            print("Hint: the Average between the answer and your guess is", avg)
                            if i == n_trial - 1:
                                print('-------------------------------------------------------')
                                print("Bruh... It was your last chance, the hint is meaningless")
                                break
                    else:
                        print("You are wrong. It is a bit high")
                elif guess < answer:
                    print("Your guess:" + str(guess) + " is too low")
                    if guess < answer/2:
                        ask = input("You are wrong, do you want a hint?? y/n ")
                        if ask.lower() == 'y':
                            print("Hint: the Average between the answer and your guess is", avg)
                            if i == n_trial - 1:
                                print('-------------------------------------------------------')
                                print("Bruh... It was your last chance, the hint is meaningless")
                                break
                    else:
                        print("You are wrong. It is a bit low")
            print('-------------------------')
            print('You lost all your chances. Just get a hint next time')
            answer = input("Do you want to try again? y/n ")
            try_again(answer.lower())
        except ValueError:
            sarcastic = ('idiot', 'moron', 'dumb', 'stupid', 'asshole', 'fool', 'twit')
            j = np.random.randint(0,len(sarcastic))
            print("You gave up, din't ya? you", sarcastic[j])
            print(",or you might typed wrong types of class such as string or blank")
        print('Did you read the notice? Please read the notice')

try:
    answer = np.random.randint(0,100)
    n_trial = int(input("How many times do you want to try: "))
    for i in range(n_trial):
        guess = int(input("Please type from 0 to 100: "))
        avg = int((guess + answer)/2)
        if guess == answer:
            again = input("Congrats!!, Do you wanna try again? y/n ")
            try_again(again)
            print("You won")
            break
        elif guess > answer:
            if guess > 2*answer:
                print("Your guess:" + str(guess) + " is too high")
                ask = input("You are wrong, do you want a hint?? y/n ")
                if ask.lower() == 'y':
                    if i == n_trial -1:
                        print('-------------------------------------------------------')
                        print("Bruh... It was your last chance, the hint is meaningless")
                        break
                    print("Hint: the Average between the answer and your guess is", avg)
            else:
                print("You are wrong.", str(guess)  ,"is a bit high")
        elif guess < answer:
            if guess < answer/2:
                print("Your guess:" + str(guess) + " is too low")
                ask = input("You are wrong, do you want a hint?? y/n ")
                if ask.lower() == 'y':
                    if i == n_trial -1:
                        print('-------------------------------------------------------')
                        print("Bruh... It was your last chance, the hint is meaningless")
                        break
                    print("Hint: the Average between the answer and your guess is", avg)
            else:
                print("You are wrong.", str(guess)  ,"is a bit low")
    print('-------------------------')
    print('You lost all your chances. Just get a hint next time')
    answer = input("Do you want to try again? y/n ")
    try_again(answer.lower())
except ValueError:
    sarcastic = ('idiot', 'moron', 'dumb', 'stupid', 'asshole', 'fool', 'twit')
    j = np.random.randint(0,len(sarcastic))
    print("You gave up, din't ya? you", sarcastic[j])
    print(",or you might typed wrong types of class such as string or blank")