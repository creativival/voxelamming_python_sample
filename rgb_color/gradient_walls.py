from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)

# ボクセルの設定
vox.set_box_size(1)
vox.set_build_interval(0.01)

# 壁のサイズ
wall_size = 10

# 壁を作成
for i in range(wall_size):
    for j in range(wall_size):
        for k in range(wall_size):
            if i == 0 or j == wall_size - 1 or k == 0:
                # 色の比率を計算
                # RGB値を計算
                r = i / (wall_size - 1)
                g = (wall_size - 1 - j) / (wall_size - 1)
                b = k / (wall_size - 1)
                vox.create_box(i, j, -k, r, g, b, 1)

# ボクセルデータを送信
vox.send_data("gradient_walls")
