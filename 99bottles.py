# 99 Bottles of Beer
# ac 09 28 17

def sing_song():
    number_of_bottles = 99
    while number_of_bottles > 0:
        print(str(number_of_bottles) + ' bottles of beer on the wall, ' +
              str(number_of_bottles) + ' bottles of beer.\n' +
              'Take one down, pass it around, ' + str(number_of_bottles - 1) +
              ' bottles of beer on the wall...')
        number_of_bottles -= 1

if __name__ == '__main__':
    sing_song()
