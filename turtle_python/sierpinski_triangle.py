import time
from turtle import Turtle, setup


def sierpinski(t, length, level):
    """
    シェルピンスキーの三角形を描画する関数

    Args:
        t (Turtle): タートルオブジェクト
        length (int): 三角形の辺の長さ
        level (int): 再帰レベル
    """
    if level == 0:
        # 三角形を描画
        for _ in range(3):
            t.forward(length)
            t.left(120)
        return

    # シェルピンスキーの三角形を再帰的に描画
    length /= 2
    sierpinski(t, length, level - 1)  # 左下の三角形
    t.forward(length)
    sierpinski(t, length, level - 1)  # 右下の三角形
    t.backward(length)
    t.left(60)
    t.forward(length)
    t.right(60)
    sierpinski(t, length, level - 1)  # 上の三角形
    t.left(60)
    t.backward(length)
    t.right(60)


# タートルグラフィックスの設定
t = Turtle()
setup(800, 600, None, None)
t.speed(0)  # 描画速度を最速に
t.penup()
t.goto(-200, -150)  # 描画開始位置
t.pendown()

# シェルピンスキーの三角形を描画 (レベル5)
sierpinski(t, 400, 5)

# 描画を保持
t.hideturtle()
time.sleep(10)
