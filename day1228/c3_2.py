name=input('名前>>')
print('{}さん、こんにちは'.format(name))
food=input('{}さんの好きな食べ物を教えて>>'.format(name))
if food=='カレー':
#インデントをそろえることでブロックと認識。以下はインデント揃ってない場合エラー
    print('素敵です')
    print('素敵です')
else:
    print('私も{}が好きです'.format(food))
