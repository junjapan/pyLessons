def input_scores(name):
    print('{}さんの試験結果を入力してね'.format(name))
    
    network=int(input('ネットワークの得点?>>'))
    database=int(input('データベースの得点?>>'))
    security=int(input('セキュリティの得点?>>'))

    scores=[network,database,security]
    return scores

def calc_average(scores):
    avg=sum(scores)/len(scores)
    return avg

def output_result(name,avg):
    print('{}さんの平均点は{}です！'.format(name,avg))

#得点入力
asagi_scores=input_scores('麻木')
matsuda_scores=input_scores('松田')
#平均点を入力
asagi_avg=calc_average(asagi_scores)
matsuda_avg=calc_average(matsuda_scores)
#結果を出力
output_result('麻木',asagi_avg)
output_result('松田',matsuda_avg)

