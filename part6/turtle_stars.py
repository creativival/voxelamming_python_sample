from voxelamming import BuildBox, Turtle

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)
# ボクセルの設定を行います
build_box.set_box_size(0.3)
build_box.set_build_interval(0.01)

# 辺の長さ
length = 60

# ボクセルを配置するため、位置と色を設定します
t = Turtle(build_box)

# 星形を回転させながら描画
for i in range(6):  # 60度ずつ回転
    t.reset()
    # タートルの色を設定します
    t.set_color(1, 1, 0, 1)  # 黄色
    t.left(i * 30)  # 回転角度を設定
    t.set_pos(0, length, 0)  # タートルの位置を設定

    # 上の頂点より星を描画
    t.down(72)
    # 星形を描画
    for _ in range(5):
        t.forward(length)
        t.down(144)

# ボクセルデータをアプリに送信します。
build_box.send_data("turtle_stars")