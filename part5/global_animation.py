from time import sleep
# voxelammingパッケージからVoxelammingクラスをインポートします
from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)
# ボクセルの設定を行います
vox.set_box_size(0.3)
vox.set_build_interval(0.01)

# ボクセルを配置するため、位置と色を設定します
for i in range(10):
    vox.create_box(-1, i, 0, r=0, g=1, b=1, alpha=1)
    vox.create_box(0, i, 0, r=1, g=0, b=0, alpha=1)
    vox.create_box(1, i, 0, r=1, g=1, b=0, alpha=1)
    vox.create_box(2, i, 0, r=0, g=1, b=1, alpha=1)

for i in range(5):
    vox.remove_box(0, i * 2 + 1, 0)
    vox.remove_box(1, i * 2, 0)

# ボクセルを配置する位置を設定します
node_positions = [
    [0, 0, 0],
    [-10, 0, 0],
    [10, 0, 0],
    [0, -20, 0],
    [0, 20, 0],
    [0, 0, -10],
    [0, 0, 10],
]

for x, y, z in node_positions:
    # ボクセルを配置するため、位置を設定します
    vox.translate(x, y, z, pitch=0, yaw=0, roll=0)
    # ボクセルデータをアプリに送信します。（位置を変えて、複数回送信）
    vox.send_data()
    # 1秒待機します
    sleep(1)

vox.animate_global(0, 0, 0, pitch=0, yaw=180, roll=0, scale=1, interval=100)

# ボクセルデータをアプリに送信します。（グローバルアニメーション）
vox.send_data()
