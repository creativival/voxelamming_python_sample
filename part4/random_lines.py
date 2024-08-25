from random import random, uniform
# voxelammingパッケージからVoxelammingクラスをインポートします
from voxelamming import Voxelamming

# 変数の設定
line_length = 50
line_num = 100

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)
# ボクセルの設定を行います
vox.set_box_size(0.2)
vox.set_build_interval(0.01)

# ボクセルを配置するため、位置と色を設定します
vox.transform(0, line_length, 0)  # 全体を上に移動

for _ in range(line_num):
    x = uniform(-line_length, line_length)
    y = uniform(-line_length, line_length)
    z = uniform(-line_length, line_length)
    r = random()
    g = random()
    b = random()
    vox.draw_line(0, 0, 0, x, y, z, r=r, g=g, b=b, alpha=1)

# ボクセルデータをアプリに送信します。
vox.send_data("random_lines")
