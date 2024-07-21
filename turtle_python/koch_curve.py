from turtle import Turtle, setup
import time


# コッホ曲線を描く関数
def koch_curve(t, length, level):
    """
    コッホ曲線を描画する関数

    Args:
        t (Turtle): タートルオブジェクト
        length (int): 線分の長さ
        level (int): 再帰レベル
    """
    if level == 0:
        t.forward(length)  # 直線を引く
        return

    # コッホ曲線を再帰的に描画
    length /= 3
    koch_curve(t, length, level - 1)
    t.left(60)
    koch_curve(t, length, level - 1)
    t.right(120)
    koch_curve(t, length, level - 1)
    t.left(60)
    koch_curve(t, length, level - 1)


# タートルグラフィックスの設定
t = Turtle()
setup(800, 600, None, None)
t.speed(0)  # 描画速度を最速に
t.penup()
t.goto(-200, 100)  # 描画開始位置
t.pendown()

# コッホ曲線を描画 (レベル4)
koch_curve(t, 400, 4)

# 描画を保持
t.hideturtle()

time.sleep(10)
