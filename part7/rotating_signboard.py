import time
from voxelamming import BuildBox

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)
# ボクセルの設定を行います
build_box.set_box_size(0.2)
build_box.set_build_interval(0)

# 看板の枠組みを作成
for i in range(16 * 10):
    for j in range(20):
        build_box.create_box(i, j, 0, 1, 1, 1)

# 看板に文字を配置
build_box.write_sentence("Voxelamming", 2, 2, 1, 1, 0, 0, 1)

# 看板を回転させる
build_box.animate(0, 0, 0, 0, 180, 0, 1, 10)

build_box.send_data("rotating_signboard")