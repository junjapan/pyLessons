scores={'network':60,'database':80,'security':50}

key=input('追加する科目名を入力')

if key in scores:
    print('すでに登録済み')
else:
    data=int(input('得点を入力してね>>'))
    scores[key]=data
print(scores)

