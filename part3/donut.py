from math import sqrt
# voxelammingパッケージからBuildBoxクラスをインポートします
from voxelamming import BuildBox

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)

# ボクセルの設定を行います
build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

# ドーナツの大きな円の半径
donut_outside_radius = 16
# ドーナツの小さな円の半径
donut_inside_radius = 8
# ドーナツの半径は、大きな円の半径と小さな円の半径の平均
donut_center_radius = (donut_outside_radius + donut_inside_radius) / 2
# ドーナツの断面の円の半径は、大きな円の半径と小さな円の半径の差の半分
donut_cross_section_radius = (donut_outside_radius - donut_inside_radius) / 2

# 上半分のみボクセルを配置（ボクセルの数を減らすため）
for i in range(0, donut_outside_radius + 1):
    # Y軸方向にドーナツの断面の円の半径の範囲内の場合
    if -donut_cross_section_radius <= i <= donut_cross_section_radius:
        # 2つの円に挟まれた部分にボクセルを配置
        # 大きな円とドーナツの半径の差、小さな円とドーナツの半径の差
        delta_radius = sqrt(donut_cross_section_radius**2 - i**2)
        # 大きな円の半径
        big_radius = int(donut_center_radius + delta_radius)
        # 小さな円の半径
        small_radius = int(donut_center_radius - delta_radius)
        print(big_radius, small_radius)

        for j in range(-big_radius, big_radius + 1):
            for k in range(-big_radius, big_radius + 1):
                # 円の式を使って、ドーナツの形になる条件を指定
                if small_radius**2 <= j**2 + k**2 < big_radius**2:
                    build_box.create_box(j, i, k, 1, 0, 1)  # 紫色でボクセルを配置

# ボクセルデータをアプリに送信します。
build_box.send_data("donut")