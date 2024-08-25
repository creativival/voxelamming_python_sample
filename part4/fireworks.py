from random import random, uniform
from random import random, uniform
from math import sin, cos, pi
from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)
# ボクセルの設定を行います
vox.set_box_size(0.2)
vox.set_build_interval(0.01)

# 花火の玉の初期位置
initial_x = 0
initial_y = 0
initial_z = 0

# 花火の玉を打ち上げる高さ
height = 30

# 花火の線の数
line_num = 3

# # 花火の玉の軌跡を描画
# for i in range(height + 1):
#     vox.create_box(initial_x, initial_y + i, initial_z, 1, 1, 0)

# 花火が開いたときの線の描画
for _ in range(line_num):
    # ランダムな角度と速度を設定
    angle = uniform(0, 2 * pi)
    speed = uniform(20, 30)

    # 1段目の線の終点座標を計算
    x1 = initial_x + speed * cos(angle)
    y1 = initial_y + height + speed * sin(angle)
    z1 = initial_z + uniform(-5, 5)

    # ランダムな色を設定
    r = random()
    g = random()
    b = random()

    # 1段目の線を描画
    vox.draw_line(initial_x, initial_y + height, initial_z, x1, y1, z1, r=r, g=g, b=b, alpha=1)

    # 2段目の分岐線を描画
    for j in range(3):
        # 分岐角度を設定
        branch_angle = j * 2 * pi / 3
        # 減衰率を設定
        speed_decay = 0.5

        # 2段目の線の終点座標を計算
        x2 = x1 + speed * speed_decay * cos(angle + branch_angle)
        y2 = y1 + speed * speed_decay * sin(angle + branch_angle)
        z2 = z1 + uniform(-5, 5)

        # 線を描画
        vox.draw_line(x1, y1, z1, x2, y2, z2, r=r, g=g, b=b, alpha=1)

# ボクセルデータをアプリに送信します。
vox.send_data("fireworks")
