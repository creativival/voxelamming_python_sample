# voxelammingパッケージからVoxelammingクラスとTurtleクラスをインポートします
from voxelamming import Voxelamming, Turtle

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)
# ボクセルの設定を行います
vox.set_box_size(0.3)
vox.set_build_interval(0.01)
vox.set_command("liteRender")  # 描画を軽くするためのコマンド

# ボクセルを配置するため、位置と色を設定します
t = Turtle(vox)

# 線の色のリスト
colors = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [0.5, 0, 0, 1],
    [0, 0.5, 0, 1],
    [0, 0, 0.5, 1],
    [0.5, 0.5, 0, 1],
    [0, 0.5, 0.5, 1],
    [0.5, 0, 0.5, 1],
    [0.5, 0.5, 0.5, 1],
]

# 色を変えながら鳥籠を描画します
for i, color in enumerate(colors):
    # 水平の角度
    polar_phi = i * 180 / len(colors)
    # タートルをリセット
    t.reset()
    # タートルの位置を設定
    t.set_color(*color)
    # タートルの水平角度を設定
    t.left(polar_phi)

    # タートルで大きな円を描画
    for _ in range(60):
        t.forward(4)
        t.up(6)

# ボクセルデータをアプリに送信します。
vox.send_data("turtle_cage")

# # タートルの位置を設定
# t.set_color(1, 0, 0, 1)
# # タートルの水平角度を設定
# t.left(90)

# # タートルで大きな円を描画
# for _ in range(15):
#     t.forward(4)
#     t.up(6)

# # ボクセルデータをアプリに送信します。
# vox.send_data("turtle_cage")
