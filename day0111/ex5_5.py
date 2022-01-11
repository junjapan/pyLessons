def int_input():
    amount=int(input('支払総額を入力>>'))
    people=int(input('参加人数を入力>>'))
    return amount,people

def calc_payment(amount,people):
    #割り勘の計算
    dnum=amount/people
    pay=dnum//100*100
    if dnum > pay:
        pay = int(pay+100)
    #幹事の支払額の計算
    payorg=amount-pay*(people-1)
    #戻り値設定
    return pay,payorg

def show_payment(pay,payorg,people):
    print('***支払額***')
    print('1人あたり{}円（{}人)、幹事は{}円です'.format(pay,people-1,payorg))

result=int_input()
result1=calc_payment(result[0],result[1])
show_payment(result1[0],result1[1],result[1])

