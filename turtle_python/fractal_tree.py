from turtle import Turtle, Screen, colormode
from random import randint

# 画面とタートルの設定
screen = Screen()
screen.setup(width=900, height=800)
screen.bgcolor("black")
colormode(255)
t = Turtle()
t.speed(0)  # 描画速度を最速に
t.penup()
t.hideturtle()
t.setheading(90)  # 上向きに設定
t.goto(0, -200)  # 描画開始位置
t.pendown()

# フラクタルツリーを描画する関数
def draw_fractal_tree(length, angle, thickness):
    """
    フラクタルツリーを描画する関数

    Args:
        length (int): 枝の長さ
        angle (int): 枝分かれ角度
        thickness (int): 枝の太さ
    """
    if length > 0 and thickness > 0: # 太さが0以下にならないように条件を追加
        # ランダムな色を設定
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        t.color(r, g, b)

        t.pensize(thickness)
        t.forward(length)
        t.right(angle)
        draw_fractal_tree(length - 10, angle, thickness - 1)
        t.left(2 * angle)
        draw_fractal_tree(length - 10, angle, thickness - 1)
        t.right(angle)
        t.backward(length)

# フラクタルツリーを描画
draw_fractal_tree(100, 20, 10)

# 画面クリックで終了
screen.exitonclick()