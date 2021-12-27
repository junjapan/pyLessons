per1={'自転車','パチンコ','旅行','温泉','競馬'}
per2={'自転車','パチスロ','旅行','温泉','競馬'}
input('心の準備ができたらenterキーを押してね>>')
match_rate=len(per1&per2)/len(per1|per2)*100
print('相性度'+str(match_rate)+'%')
