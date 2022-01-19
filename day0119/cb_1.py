from math import pow
print(pow(10,2))
def funcA(z):
    ans=z*2
    print(ans)

def funcB(x,y):
    z=x+y
    funcA(z)

x=10
y=20
funcB(10,20)


print('hello')

my_list=[10,20,30]

x=10
if(x<10):
    print('hoge')
else:
    print('foo')

x=10
print('こんにちは')

print(x)

print('hello'+str(x))

print('hello' * 5)


def hello():
    print('Hello')
hello()

def hello(x):
    print('Hello,' + x)
hello('1')

x=10
y=1
ans=x/y


if x >= 100:
    print('hoge')
else:
    print('foo')

if x >= 100:
        print('hoge')
        print('foo')

my_list=[10,20,30]
my_list[2]

my_dict={'hoge':1,'foo':2}
print(my_dict['foo'])

x='100'
x=int(x)

a=100

def hoge():
    global a
    print(a)
    a=10
hoge()
print(a)

x=0
while x<10:
    print('hello')
    x += 1

try:
    price = int(input('料金を入力>>'))
    number = int(input('人数を入力>>'))
    print('一人あたり{}円です'.format(price/number))
#except ValueError:
#    print('料金または人数は整数を入力してください')
#except ZeroDivisionError:
#    print('人数にゼロは入力しないでください。')
except:
    print('適せるな値を入力してください')
else:
finally:
    print('ok')
print('プログラムを終了します')
