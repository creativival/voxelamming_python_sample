from time import sleep
from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)
# ボクセルの設定を行います
vox.set_box_size(0.4)
vox.set_build_interval(0)  # インターバルを0にする

# 土台
for i in range(-16, 17):
    for j in range(-16, 17):
        if i ** 2 + j ** 2 < 16 ** 2:
            vox.create_box(i, 0, j, r=0.8, g=0.5, b=0.2)

# 支柱
for i in range(10):
    vox.create_box(0, i + 1, 0, r=0.6, g=0.3, b=0.1)

# 回転軸
vox.create_box(0, 11, 0, r=0.9, g=0.9, b=0.9)


# 馬を作成する関数
def create_horse(x, y, z, r, g, b):
    vox.create_box(x, y + 3, z, r=r, g=g, b=b)  # 頭
    vox.create_box(x, y + 2, z, r=r, g=g, b=b)  # 体
    vox.create_box(x + 1, y + 1, z, r=r, g=g, b=b)  # 足
    vox.create_box(x - 1, y + 1, z, r=r, g=g, b=b)  # 足


# 馬の初期位置
horse_positions_and_colors = [
    [8, 1, 8, 1, 0, 0],
    [-8, 1, 8, 0, 1, 0],
    [8, 1, -8, 0, 0, 1],
    [-8, 1, -8, 1, 1, 0]
]

# 馬のノードを作成
for positions_and_colors in horse_positions_and_colors:
    create_horse(*positions_and_colors)

vox.send_data("merry_go_round")
sleep(1)

# メリーゴーランドを回転させる
for i in range(10):
    # メリーゴーランドを回転させる（グローバルアニメーション）
    # 回転できる角度は180度までです。
    vox.animate_global(0, 0, 0, pitch=0, yaw=180, roll=0, scale=1, interval=1)
    # ボクセルデータをアプリに送信します。（グローバルアニメーション）
    vox.send_data()
    sleep(1.1)
