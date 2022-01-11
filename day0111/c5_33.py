name='松田'

def change_name():
    global name
    name = '麻木'
    hello()

def hello():
    print('こんにちは'+name+'さん')

change_name()
#hello()
