from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)

# ボクセルの設定を行います
vox.set_box_size(0.5)
vox.set_build_interval(0.01)

# 円錐の高さ
height = 15

# 各段の幅を計算
for i in range(height):
    radius = height - i + 5  # i段目の半径
    for j in range(-radius, radius + 1):
        for k in range(-radius, radius + 1):
            # 台形を作る条件
            if (radius - 1) ** 2 <= j ** 2 + k ** 2 < radius ** 2:
                vox.create_box(j, i, k, 1, 0, 0)  # 赤色でボクセルを配置

# ボクセルデータをアプリに送信します。
vox.send_data("cone")
