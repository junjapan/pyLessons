import turtle
t=turtle.Turtle() # インスタンス作成
t.speed(1)
t.shape('turtle') # 見た目を亀に
for i in range(5):
    t.forward(100)
    t.right(144)
#t.home()
turtle.mainloop() # 実行を監視
