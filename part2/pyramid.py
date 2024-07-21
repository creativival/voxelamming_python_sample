from voxelamming import BuildBox

room_name = "1000"
build_box = BuildBox(room_name)

build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

step_num = 20
for i in range(step_num): # 段数
    for j in range(i * 2 + 1): # 各段のボクセル数
        build_box.create_box(j - i, step_num - i, 0)  # x座標を調整して中央に配置

build_box.send_data("pyramid")