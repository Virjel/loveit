n = 1
my_list = []
unwanted_letters = []
game_list = []
name = input('please enter your name: ')
name1 = name.upper()
names = input('please enter your partner name: ')
name2 = names.upper()
for item in name1:
    if item not in name2:
        if item != ' ':
            my_list.append(item)
for value in name2:
    if value not in name1:
        if value != ' ':
            my_list.append(value)
print(f'Unmatched letters are : {my_list}')
number = len(my_list)
print(f'Unmatched letters counts to :{number}')
needed = number*number
game = ['f', 'l', 'a', 'm', 'e', 's']
for i in range(0, needed):
    game_list.append(game)
for value in game_list:
    for item in value:
        if item not in unwanted_letters:
            if n == number:
                unwanted_letters.append(item)
                n = 1
            else:
                n += 1
fetch = len(unwanted_letters)-1
sucess = (unwanted_letters[fetch])
if sucess == 'f':
    print(f'friend : Hey {name}!! {names} is your friend')
if sucess == 'l':
    print(f'love : Hey {name}!! {names} is your loveable one')
if sucess == 'a':
    print(f'affection : Hey {name}!! {names} is more affectionate on you,hope you are lucky!!')
if sucess == 'm':
    print(f'marriage : Hey {name}!! {names} is going to marry you soon\n    HAHAHA!! coool man,just for fun')
if sucess == 'e':
    print(f'enemy : Hey {name}!! {names} is your enemy\n    Is it soo??')
if sucess == 's':
    print(f'sister : Hey {name}!! {names} is your loveable Sister')