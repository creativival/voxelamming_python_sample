from time import sleep
from random import random, uniform
from math import sin, cos, pi
from voxelamming import BuildBox

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)
# ボクセルの設定を行います
build_box.set_box_size(1)
build_box.set_build_interval(0)  # インターバルを0にする

# 爆発の中心座標
center_x = 0
center_y = 0
center_z = 0

# 破片の数
fragment_num = 100

# 破片を配置
build_box.create_box(0, 0, 0, 1, 0, 0)

# 各破片のノードを作成
for i in range(fragment_num):
    # ランダムな方向と速度を設定
    angle_h = uniform(0, 2 * pi)  # 水平方向の角度
    angle_v = uniform(0, pi / 2)  # 垂直方向の角度
    speed = uniform(50, 100)

    # 移動距離を計算
    x = speed * cos(angle_h) * sin(angle_v)
    y = speed * cos(angle_v)
    z = speed * sin(angle_h) * sin(angle_v)

    # ランダムな色を設定
    r = random()
    g = random()
    b = random()

    # アニメーションを設定
    build_box.animate(x, y, z, interval=100)  # 100フレームかけて移動

    # ボクセルデータをアプリに送信します。
    build_box.send_data()
    sleep(0.5)  # 0.5秒待機