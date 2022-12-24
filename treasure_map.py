row1 = ['⬜️️','⬜️️','⬜️️']
row2 = ['⬜️️','⬜️️','⬜️️']
row3 = ['⬜️️','⬜️️','⬜️️']
map = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}')

position = input('Where do you want to put the treasure? ')

column = int(position[0]) - 1
row = int(position[1]) - 1

if row > 2 and column > 2:
    print('Invalid coordinates')
elif row > 2:
    print('Invalid row coordinate')
elif column > 2:
    print('Invalid column coordinate')
else:
    selected_row = map[row]
    selected_row[column] = 'X'

print(f'{row1}\n{row2}\n{row3}')