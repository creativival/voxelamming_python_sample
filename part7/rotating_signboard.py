import time
from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)
# ボクセルの設定を行います
vox.set_box_size(0.2)
vox.set_build_interval(0)

# 看板の枠組みを作成
for i in range(16 * 10):
    for j in range(20):
        vox.create_box(i, j, 0, 1, 1, 1)

# 看板に文字を配置
vox.write_sentence("Voxelamming", 2, 2, 1, 1, 0, 0, 1)

# 看板を回転させる
vox.animate(0, 0, 0, 0, 180, 0, 1, 10)

vox.send_data("rotating_signboard")
