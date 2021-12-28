la=int(input('国語の点数を入力>>'))
ma=int(input('算数の点数を入力>>'))
sc=int(input('理科の点数を入力>>'))
so=int(input('社会の点数を入力>>'))
en=int(input('英語の点数を入力>>'))
test=[la,ma,sc,so,en]
print(f'合計点は{sum(test)}点です')
print(f'平均点は{sum(test)/len(test)}点です')
