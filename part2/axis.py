# voxelammingパッケージからVoxelammingクラスをインポートします
from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)

# ボクセルのサイズを設定します
vox.set_box_size(0.1)
# ボクセルの配置間隔を設定します
vox.set_build_interval(0.01)

# ボクセルを配置するため、位置と色を設定します
for i in range(100):
    vox.create_box(i, 0, 0, r=1, g=0, b=0, alpha=1)
    vox.create_box(0, i, 0, r=0, g=1, b=0, alpha=1)
    vox.create_box(0, 0, i, r=0, g=0, b=1, alpha=1)

# ボクセルデータをアプリに送信します。
vox.send_data("axis")
