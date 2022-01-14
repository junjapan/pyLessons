scores1=[80,40,50]
scores2=[80,40,50]
scores3=scores1
print('scores1のidentity:{}'.format(id(scores1)))
print('scores2のidentity:{}'.format(id(scores2)))

print('中身確認')
if scores1 == scores2:
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')

if id(scores1) == id(scores3):
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')

print('identity確認')
if id(scores1) == id(scores2):
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')

