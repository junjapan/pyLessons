import turtle
t=turtle.Turtle() # インスタンス作成
t.speed(1)
t.shape('turtle') # 見た目を亀に
t.color('blue')
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.penup()
t.home()
turtle.mainloop() # 実行を監視
