from voxelamming import BuildBox

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)

# ボクセルの設定を行います
build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

# 円錐の高さ
height = 15

# 各段の幅を計算
for i in range(height):
    radius = height - i + 5  # i段目の半径
    for j in range(-radius, radius + 1):
        for k in range(-radius, radius + 1):
            # 台形を作る条件
            if (radius - 1) ** 2 <= j**2 + k**2 < radius**2:
                build_box.create_box(j, i, k, 1, 0, 0)  # 赤色でボクセルを配置

# ボクセルデータをアプリに送信します。
build_box.send_data("cone")