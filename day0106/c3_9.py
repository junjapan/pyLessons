score=int(input('試験の点数を入力してね>>'))
if score < 0 or score > 100:
    print('異常な得点です')
    print('入力しなおしてね')
elif score >= 60:
    print('合格！')
    print('よくがんばりました')
else:
    print('残念ながら不合格')
    print('追試を受けてください')

