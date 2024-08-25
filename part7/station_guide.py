import time
from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)
# ボクセルの設定を行います
vox.set_box_size(0.3)
vox.set_build_interval(0.01)

# 矢印フォント
arrow_font = [
    "0,0,0,0,0,0,0,0,0,0,0",
    "0,0,0,0,0,0,0,0,0,0,0",
    "0,0,0,0,0,1,0,0,0,0,0",
    "0,0,0,0,1,1,0,0,0,0,0",
    "0,0,0,1,1,1,0,0,0,0,0",
    "0,0,1,1,1,1,0,0,0,0,0",
    "0,1,1,1,1,1,1,1,1,1,1",
    "1,1,1,1,1,1,1,1,1,1,1",
    "0,1,1,1,1,1,1,1,1,1,1",
    "0,0,1,1,1,1,0,0,0,0,0",
    "0,0,0,1,1,1,0,0,0,0,0",
    "0,0,0,0,1,1,0,0,0,0,0",
    "0,0,0,0,0,1,0,0,0,0,0",
    "0,0,0,0,0,0,0,0,0,0,0",
    "0,0,0,0,0,0,0,0,0,0,0",
    "0,0,0,0,0,0,0,0,0,0,0"
]

# 案内表示の情報
guide_info_list = [
    {"sentence": "山手線", "color": [0, 1, 0], "direction": -30},
    {"sentence": "京浜東北線", "color": [0, 0, 1], "direction": 0},
    {"sentence": "中央線", "color": [1, 0.5, 0], "direction": 30},
    {"sentence": "東海道線", "color": [1, 0.5, 0], "direction": 60}
]

# 円柱の半径
cylinder_radius = 8
# 円柱の高さ
cylinder_height = 16

# 文字のサイズ
character_base_size = 0.3

# 円柱を作成
for i in range(cylinder_height):
    for j in range(2):
        for k in range(2):
            vox.create_box(j, i, k, 0.8, 0.8, 0.8)

# 案内表示を配置
for i, guide_info in enumerate(guide_info_list):
    sentence = guide_info["sentence"]
    color = guide_info["color"]
    direction = guide_info["direction"]

    vox.transform(0, i * 16, 0, 0, direction, 0)

    # 矢印を描画
    for y, line in enumerate(arrow_font):
        for x, bit in enumerate(line.split(',')):
            if bit == "1":
                vox.create_box(x + 6, y, 0, 1, 1, 0)  # 黄色で矢印を描画

    # 文字列を描画
    vox.write_sentence(sentence, 20, 0, 0, *color, 1)

    vox.send_data(sentence)
    time.sleep(1)
