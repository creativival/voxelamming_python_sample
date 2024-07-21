# voxelammingパッケージからBuildBoxクラスをインポートします
from voxelamming import BuildBox

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)

# ボクセルのサイズを設定します
build_box.set_box_size(0.1)
# ボクセルの配置間隔を設定します
build_box.set_build_interval(0.01)

# ボクセルを配置するため、位置と色を設定します
for i in range(100):
    build_box.create_box(i, 0, 0, r=1, g=0, b=0, alpha=1)
    build_box.create_box(0, i, 0, r=0, g=1, b=0, alpha=1)
    build_box.create_box(0, 0, i, r=0, g=0, b=1, alpha=1)

# ボクセルデータをアプリに送信します。
build_box.send_data("axis")
