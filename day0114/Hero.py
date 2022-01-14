class Hero:
    def __init__(self,name,hp=100):
        self.name=name
        self.hp=hp
    name='松田'
    hp=100
    def sleep(self,hours):
        print('{}は{}時間寝た！'.format(self.name,hours))
        self.hp += hours

#ゲーム開始
print('スッキリファンタジーⅦ　～金色の理想郷～')
h=Hero('じゅんいち',200)
h1=Hero('じゅんいち')
h.sleep(3)
print('{}のＨＰは現在{}です'.format(h.name,h.hp))
print('{}のＨＰは現在{}です'.format(h1.name,h1.hp))
