n_smile = 1
while n_smile >= 1:
    a = input('칭찬 y/n? ')
    if a == 'y':
        n_smile += 1
        print('^','_'*n_smile,'^')
    else:
        n_smile -= 1
        if n_smile == 0:
            print('뒤질래?')
            break
        else:
            print('^', '_'*n_smile, '^')



cmd = ""
engine = 0
while True:
    cmd = input("What would you say ")
    if cmd.lower() == 'go':
        engine += 1
        print(engine)
    elif cmd.lower() == 'help':
        print('start - to start the car\n',
              'else - to stop the car\n',
              'quit - to quit the game')
    else:
        engine -= 1
        print(engine)
        if engine == 0:
            print('Fuck off')
            break