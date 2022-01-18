import random

print('数当てゲームを始めます。３桁の数を当ててね！')
answer=[random.randint(0,9) for i in range(3)]
#prediction=[ int(input(f'{i}桁目の予想を入力(0-9)>>')) for i in range(1,4)]

#print(answer)
#print(prediction)

hit=0
ball=0
count1=0
count2=0

while True:
    prediction=[ int(input(f'{i}桁目の予想を入力(0-9)>>')) for i in range(1,4)]
    for ans in answer:
        print(ans)
        for pre in prediction:
            print(pre)
            if count1==count2 and ans==pre:
                hit += 1
            elif count1==count2:
                ball += 1
            count1 += 1
        count2 += 1
    print('{}ヒット、{}ボール'.format(hit,ball))
    print('答えは{}でした'.format(answer))
    if hit == len(answer):
        print('正解')
        break
    else:
        res=input('続けますか？1:続ける2:終了>>')
        if res=='2':
            print('終了')
            break

