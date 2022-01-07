def hello(name):
    print('こんにちは。{}です'.format(name))
hello('麻木')
hello('渡辺')

print()
def profile(name,age,hobby):
    print('私の名前は{}です。'.format(name))
    print('年齢は{}歳です。'.format(age))
    print('趣味は{}です。'.format(hobby))

profile('渡辺',24,'カフェ巡り')

print()

def plus(x,y):
    answer=x+y
    return answer
answer=plus(100,50)
print('足し算の結果は{}です'.format(answer))
