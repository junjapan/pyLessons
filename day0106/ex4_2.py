count=1
print('カレーを召し上がれ')
while True:
    print(f'{count}皿のカレーを食べた')
    ans = input('おかわりはいかが>>')
    if ans == 'y':
        count += 1
    else:
        print('ごちそうさまでした')
        break

