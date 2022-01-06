print('すべての質問にyまたはnで答えて')
okane_aruka=input('お金に余裕はあるか？>>')
if okane_aruka == 'y':
    onaka_suiteruka = input('お腹がすごく空いてますか？>>')
    nomitai_kibunka = input('ビールを飲みたいですか？>>')
    if onaka_suiteruka == 'y' and nomitai_kibunka == 'y':
        print('焼肉はいかが')
    elif onaka_suiteruka == 'y':
        print('カレーはいかが')
    elif nomitai_kibunka == 'y':
        print('焼き鳥はいかが')
    else:
        print('パスタはいかが')
    yashoku_iruka = input('夜食は必要？>>')
    if yashoku_iruka == 'y':
        print('コンビニのチキンはいかが')
else:
    print('家で食べましょう')

