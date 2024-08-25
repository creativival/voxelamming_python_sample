# voxelammingパッケージからVoxelammingクラスをインポートします
from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)

# ボクセルを配置するため、位置と色を設定します
for i in range(20):
    vox.create_box(0, i, 0)

# ボクセルデータをアプリに送信します。
vox.send_data("sample")
