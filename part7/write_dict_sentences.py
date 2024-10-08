import time
# voxelammingパッケージからVoxelammingクラスをインポートします
from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)
# ボクセルの設定を行います
vox.set_build_interval(0.01)

character_base_size = 0.3
# 文を配置するための辞書のリスト
sentence_dict_list = [
    {"sentence": "こんにちは", "position": [0, 0, 0], "rotation": [0, 0, 0], "color": [0, 1, 0, 1], "scale": 1},
    {"sentence": "Hello World", "position": [0, 16, 0], "rotation": [0, 0, 0], "color": [1, 0, 0, 1], "scale": 1},
    {"sentence": "Voxel", "position": [0, 16, 0], "rotation": [0, 60, 0], "color": [0, 0, 1, 1], "scale": 1.5},
    {"sentence": "ボクセル", "position": [0, 16, 0], "rotation": [0, 0, 75], "color": [1, 1, 0, 1], "scale": 2},
]

# ボクセルを配置するため、位置と色を設定します
for sentence_dict in sentence_dict_list:
    # 辞書から値を取得します
    sentence_str = sentence_dict["sentence"]
    position = sentence_dict["position"]
    rotation = sentence_dict["rotation"]
    color = sentence_dict["color"]
    scale = sentence_dict["scale"]

    # ボクセルを配置します
    vox.set_box_size(character_base_size * scale)
    vox.transform(*position, *rotation)
    vox.write_sentence(sentence_str, 0, 0, 0, *color)

    # ボクセルデータをアプリに送信します。
    vox.send_data(sentence_str)
    time.sleep(1)
