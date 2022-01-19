for i in range(10):
    if i==7:
        break
    print(i)
else:
    print('完了')


import random

#ansList=[random.randint(0,9) for i in range(10)]
ansList=[random.randrange(10) for i in range(10)]
#以下はランダムの奇数を設定
ansList=[random.randrange(1,10,2) for i in range(10)]

print(ansList)

for i in range(len(ansList)):
    if ansList[i] == 7:
        print(f'index{i}に７はありました')
        break
else:
    print('７はありませんでした')

#先生のもう一つの回答
#data=[random.randint(0,9) for i in range(10)]
#print(data)
#if 7 in data:
#    print(f'index{data.index(7)}に７はありました')
#else:
#    print('7はありませんでした')
