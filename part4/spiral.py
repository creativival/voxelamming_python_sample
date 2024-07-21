from random import random, uniform
from math import sin, cos, pi
from voxelamming import BuildBox

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)
# ボクセルの設定を行います
build_box.set_box_size(0.2)
build_box.set_build_interval(0.01)

# 螺旋の半径
radius = 10
# 螺旋の高さ
height = 30
# 角度
angle = 0
# 高さ方向の現在位置
current_height = 0

# 螺旋の始点座標
x1 = 0
y1 = 0
z1 = 0

# 螺旋を描く
while current_height < height:
    # x, y, z 座標を計算
    x2 = radius * cos(angle)
    y2 = current_height
    z2 = radius * sin(angle)

    # ランダムな色を設定
    r = random()
    g = random()
    b = random()

    # 線を描画
    build_box.draw_line(x1, y1, z1, x2, y2, z2, r=r, g=g, b=b, alpha=1)

    # 始点座標を更新
    x1 = x2
    y1 = y2
    z1 = z2

    # 角度と高さを更新
    angle += 0.5
    current_height += 0.5

# ボクセルデータをアプリに送信します。
build_box.send_data("spiral")