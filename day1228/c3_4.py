name=input('名前>>')
print('{}さん、こんにちは'.format(name))
food=input('{}さんの好きな食べ物を教えて>>'.format(name))
# inにより含むかどうかを判定
if 'カレー' in food:
    print('素敵')
else:
    print('私も{}が好きです'.format(food))

n=10
if n in [5,10,15]:
    print('ok')
else:
    print('ng')

key='red'
if key in {'red':'赤','blue':'青'}:
    print('ok')
else:
    print('ng')

